from src.channel import Channel
import json
class Video(Channel):

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.video = self.get_service().videos().list(id=self.video_id,
                                                      part='snippet,statistics,contentDetails,topicDetails').execute()
        self.id = self.video["items"][0]['id']
        self.title = self.video["items"][0]['snippet']["title"]
        self.viewCount = self.video["items"][0]['statistics']["viewCount"]
        self.likeCount = self.video["items"][0]['statistics']["likeCount"]

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