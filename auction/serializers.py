from rest_framework import serializers
from auction.models import Bid

class BidCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['item', 'amount']
