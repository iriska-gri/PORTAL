import json
import base64
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
import jwt
import redis

class WatcherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.client = redis.Redis(host='127.0.0.1')
        user = parse_qs(self.scope["query_string"].decode("utf8"))["token"][0]
        user = jwt.decode(user, options={"verify_signature": False})
        
        # self.client.sadd('online',json.dumps(user['user'],indent=4))
        self.room_group_name = "online"        
        self.client.hset('online',str(self.channel_name), user['user']['login'] )
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        online = [x.decode('utf-8') for x in  self.client.hvals("online")]
        await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': {'action':'onliner','data':online}
        })

        await self.accept()
     

    async def disconnect(self, close_code):
        # Leave room group
        self.client.hdel("online", self.channel_name)
        
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )
       
        online = [x.decode('utf-8') for x in  self.client.hvals("online")]
        await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': {'action':'onliner','data':online}
        })

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))