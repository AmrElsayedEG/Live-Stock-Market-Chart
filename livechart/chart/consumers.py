import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
class ChartConsumer(WebsocketConsumer):
    def connect(self):
        self.groupname='dashboard'
        async_to_sync(self.channel_layer.group_add)(
            self.groupname,
            self.channel_name,
            )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        self.accept()

    # Receive message from WebSocket
    def receive(self, text_data):
        #text_data_json = json.loads(text_data)
        datapoint = json.loads(text_data)
        val = datapoint['value']
        async_to_sync(self.channel_layer.group_send)(
            self.groupname,{
                'type':'deprocessing',
                'value':val
                }
            )
        print(text_data)
    def deprocessing(self,event):
        valOther = event['value']
        self.send(text_data=json.dumps({'value':valOther}))
