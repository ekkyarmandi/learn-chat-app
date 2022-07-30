from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name = "general"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name # generated autmatically by system
        )
        self.accept()

    def receive(self,text_data):
        payloads = json.loads(text_data)
        message = payloads.get('message')
        
        ### send back to the socket server
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message', # need to be specied below
                'message': message
            }
        )

    def chat_message(self,event):
        message = event.get("message")
        self.send(text_data=json.dumps({
            "type": "chat",
            "message": message
        }))