# Discord Bots

## TL;DR
This is a small project to test out some ideas in building simple discord bots for personal interest such as YouTube,
Twitter following functions.

## YouTube Followers
It mainly uses the API from [here](https://developers.google.com/youtube). For example you can find the search list API
[here](https://developers.google.com/youtube/v3/docs/search/list). And you will need to create an API key and fulfill 
other pre-req following [here](https://developers.google.com/youtube/v3/getting-started).

### To find a Channel ID
1. visit the channel page you're interested in on YouTube, e.g. https://www.youtube.com/@JamesJani
2. Right-click on your browser and click View Page Source.
3. Search (Ctrl-F) for https://www.youtube.com/channel/ in the page source.
4. The channel ID will appear directly after the /channel/ text in the URL path.
Reference can be found [here](https://mixedanalytics.com/blog/find-a-youtube-channel-id/)
