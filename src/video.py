from src.channel import Channel
import json


class Video(Channel):

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        try:
            self.video = self.get_service().videos().list(id=self.video_id,
                                                          part='snippet,statistics,contentDetails,topicDetails').execute()
            self.id = self.video["items"][0]['id']
            self.title = self.video["items"][0]['snippet']["title"]
            self.view_count = self.video["items"][0]['statistics']["viewCount"]
            self.like_count = self.video["items"][0]['statistics']["likeCount"]
        except Exception:
            self.id = None
            self.title = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f"{self.title}"

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.video, indent=2, ensure_ascii=False))


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.video, indent=2, ensure_ascii=False))
