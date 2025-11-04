from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AuctionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.item_id = self.scope['url_route']['kwargs']['item_id']
        self.room_group_name = f"auction_{self.item_id}"

        # Join the auction group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # (Optional) You could handle messages from client here
        pass

    async def send_new_bid(self, event):
        """Receive message from group and send to WebSocket"""
        await self.send(text_data=json.dumps({
            'new_price': event['new_price']
        }))
