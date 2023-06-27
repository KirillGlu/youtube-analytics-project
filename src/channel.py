import json
import os

from googleapiclient.discovery import build

import isodate

api_key: str = os.getenv('API_KEY')
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.id = self.channel["items"][0]['id']
        self.title = self.channel["items"][0]['snippet']["title"]
        self.description = self.channel["items"][0]['snippet']["description"]
        self.url = self.channel["items"][0]['snippet']["customUrl"]
        self.viewCount = self.channel["items"][0]['statistics']["viewCount"]
        self.subscriberCount = self.channel["items"][0]['statistics']["subscriberCount"]
        self.video_count = self.channel["items"][0]['statistics']["videoCount"]

    def __str__(self):
        return f"{self.title} (https://www.youtube.com/channel/{self.id})"

    @property
    def channel_id(self):
        return f"{self.__channel_id}"

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, data):
        with open(data, "a") as f:
            json.dump(self.channel, f)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def __add__(self, other):
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __lt__(self, other):
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        return self.subscriberCount <= other.subscriberCount

    def __gt__(self, other):
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        return self.subscriberCount >= other.subscriberCount
