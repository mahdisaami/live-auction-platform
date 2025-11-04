from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from auction.models import AuctionItem, Bid
from auction.serializers import BidCreateSerializer

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class PlaceBidView(APIView):
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = BidCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = get_object_or_404(AuctionItem, id=serializer.validated_data['item'].id)
        amount = serializer.validated_data['amount']

        # Lock the row until transaction completes
        item = AuctionItem.objects.select_for_update().get(id=item.id)

        if timezone.now() > item.ends_at:
            return Response({"error": "Auction ended"}, status=status.HTTP_400_BAD_REQUEST)

        if amount <= item.current_price:
            return Response({"error": "Bid must be higher than current price"}, status=status.HTTP_400_BAD_REQUEST)

        # Save the new bid
        Bid.objects.create(item=item, amount=amount)
        item.current_price = amount
        item.save()


        # after item.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"auction_{item.id}",
            {
                "type": "send_new_bid",
                "new_price": str(item.current_price)
            }
        )

        return Response({"message": "Bid placed successfully", "new_price": str(item.current_price)})
