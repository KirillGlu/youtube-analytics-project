from src.channel import Channel
import json
import datetime
import isodate


class PlayList(Channel):

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_info = self.get_service().playlists().list(id=playlist_id,
                                                                 part='snippet',
                                                                 maxResults=50,
                                                                 ).execute()

        self.title = self.playlist_info["items"][0]['snippet']["title"]
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_info["items"][0]['id']
        self.playlist_videos = self.get_service().playlistItems().list(playlistId=playlist_id,
                                                                       part='contentDetails',
                                                                       maxResults=50).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                               id=','.join(self.video_ids)).execute()

    @property
    def total_duration(self):
        delta = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            delta += duration
        return delta

    def show_best_video(self):
        like_count = []
        for video in self.video_response['items']:
            like_count.append(video['statistics']['likeCount'])
        temp_index = like_count.index(max(like_count))
        like_videos = self.video_response['items'][temp_index]['id']
        return f"https://youtu.be/{like_videos}"

