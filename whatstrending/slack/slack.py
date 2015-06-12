import time
import urllib.request
import json
from websocket import create_connection

from whatstrending import settings

class SlackAPI:
    def get_api_data(self):
        params = {}
        params['token'] = self.token
        url_values = urllib.parse.urlencode(params)
        url="https://slack.com/api/rtm.start"
        url = url + "?" + url_values
        data = urllib.request.urlopen(url).read()
        return json.loads(data.decode("utf8"))

    def get_channel_id(self, channel_name):
        for channel in self.api_data['channels']:
            if channel['name'] == channel_name:
                return channel['id']
        return ""

    def get_group_id(self, group_name):
        for group in self.api_data['groups']:
            if group['name'] == group_name:
                return group['id']
        return ""

    def get_user_id(self, user_name):
        for user in self.api_data['users']:
            if user['name'] == user_name:
                return user['id']
        return ""

    def get_channel_by_id(self, id):
        for channel in self.api_data['channels']:
            if channel['id'] == id:
                return channel['name']
        return ""

    def get_group_by_id(self, id):
        for group in self.api_data['groups']:
            if group['id'] == id:
                return group['name']
        return ""

    def get_user_by_id(self, id):
        for user in self.api_data['users']:
            if user['id'] == id:
                return user['id']
        return ""

    def generic_get_by_id(self, id):
        channelId = self.get_channel_by_id(id)
        groupID = self.get_group_by_id(id)
        userID = self.get_user_by_id(id)
        if channelId != "":
            return channelId
        if groupID != ""
            return groupID
        if userID != ""
            return userID
        return ""

    def send_message_to_channel(self, channel_name, message_text):
        message = {
            'id':self.event_id,
            'type': 'message',
            'channel': self.get_channel_id(channel_name),
            'text': message_text}
        encoded_message = json.dumps(message)
        self.ws.send(encoded_message)
        self.event.id = self.event.id + 1

    def send_message_to_group(self, group_name, message_text):
        message = {
            'id':self.event_id,
            'type': 'message',
            'channel': self.get_group_id(group_name),
            'text': message_text}
        encoded_message = json.dumps(message)
        self.ws.send(encoded_message)
        self.event.id = self.event.id + 1

    def send_message_to_user(self, user_name, message_text):
        message = {
            'id':self.event_id,
            'type': 'message',
            'channel': self.get_user_id(user_name),
            'text': message_text}
        encoded_message = json.dumps(message)
        self.ws.send(encoded_message)
        self.event.id = self.event.id + 1

    def receive(self):
        while True:
            mdata = json.loads(self.ws.recv())
            if ('type' in mdata) and mdata['type'] == 'message':
                if not ('reply_to' in mdata):
                    return {'message': mdata['text'], id: mdata['user']}

    def __init__(self, bot_token):
        self.token = bot_token
        self.api_data = self.get_api_data()
        self.ws = create_connection(self.api_data['url'])
        self.event_id = 1
