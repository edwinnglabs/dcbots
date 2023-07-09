"""Pre-req:
1. find Dev/API Key from YouTube API Console
2. find Channel id in channel page and click "view-source"
3. find webhook url from discord setting of the specific webhook
"""

import argparse
from dcbots.bots import YouTubeChannelFollower


parser = argparse.ArgumentParser()
parser.add_argument("-key", "--dev-key", help="Developer/API Key")
parser.add_argument("-url", "--webhook-url", help="Discord Webhook URL")
parser.add_argument("-id", "--channel-id", help="Youtube Channel ID")
parser.add_argument("--max-results", help="Max results", default=5)

args = parser.parse_args()
ytcf = YouTubeChannelFollower(
    dev_key=args.dev_key,
    max_results=args.max_results,
    channel_id=args.channel_id,
    webhook_url=args.webhook_url,
)
ytcf.post_update()
