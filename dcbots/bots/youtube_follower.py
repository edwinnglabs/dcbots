from .base import DiscordBot
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from discordwebhook import Discord

from typing import Dict, Optional, Literal, Any


class YouTubeChannelFollower(DiscordBot):
    # class constants
    _YOUTUBE_API_SERVICE_NAME = "youtube"
    _YOUTUBE_API_VERSION = "v3"
    _Content_Header = "今日推介"
    _Content_Title_Label = "題目"
    _Content_Link_Label = "鏈結"

    def __init__(
        self,
        dev_key: str,
        max_results: int,
        channel_id: str,
        webhook_url: str,
        recency: Optional[Dict[str, int]] = None,
        reference_datetime: Literal["now", "yesterday"] = "now",
        search_list_args: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__()
        self.dev_key = dev_key
        self.max_results = max_results
        self.channel_id = channel_id
        self.webhook_url = webhook_url
        self.reference_datetime = reference_datetime
        if recency is None:
            self.recency = {"days": 1}
        else:
            self.recency = recency

        if search_list_args is None:
            self.search_list_args = dict()
        else:
            self.search_list_args = search_list_args

    def _search_and_list(self):
        # to RFC 3339 format for google
        if self.reference_datetime == "now":
            ref_dt = datetime.now()
        elif self.reference_datetime == "yesterday":
            ref_dt = datetime.now() - timedelta(days=1)
        else:
            print("Invalid reference_datetime.")

        published_after = ref_dt - timedelta(**self.recency)
        published_after_iso = (
            published_after.astimezone().replace(microsecond=0).isoformat()
        )
        youtube = build(
            YouTubeChannelFollower._YOUTUBE_API_SERVICE_NAME,
            YouTubeChannelFollower._YOUTUBE_API_VERSION,
            developerKey=self.dev_key,
        )

        # Check this page: https://developers.google.com/youtube/v3/docs/search/list
        # for docs for all the input args and output types
        search_response = (
            youtube.search()
            .list(
                part="id,snippet",
                maxResults=self.max_results,
                type="video",
                eventType="completed",
                order="date",
                channelId=self.channel_id,
                publishedAfter=published_after_iso,
                **self.search_list_args,
            )
            .execute()
        )

        return search_response

    def _generate_content(self, search_response: Dict[str, Any]):
        discord = Discord(url=self.webhook_url)
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                url = "https://www.youtube.com/watch?v={}".format(
                    search_result["id"]["videoId"]
                )
                content = ":heart_hands: {} :heart_hands:\n".format(
                    YouTubeChannelFollower._Content_Header
                )
                content += "{}: {}\n{}: {}\n".format(
                    YouTubeChannelFollower._Content_Title_Label,
                    search_result["snippet"]["title"],
                    YouTubeChannelFollower._Content_Link_Label,
                    url,
                )
                # content += "View Count: {}".format(search_result['statistics']['viewCount'])
                print(search_result["snippet"].keys())
                # discord.post(content=content)

    def post_update(self):
        search_response = self._search_and_list()
        self._generate_content(search_response=search_response)
