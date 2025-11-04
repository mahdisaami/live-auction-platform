from django.urls import path

from auction.views import PlaceBidView

urlpatterns = [
    path("bid/", PlaceBidView.as_view(), name="place-bid"),
]
