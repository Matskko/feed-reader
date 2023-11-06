import feedparser

feed_url = "https://github.com/acryldata/datahub-helm/releases.atom"

feed = feedparser.parse(feed_url)

try:
    print("feed title:", feed.feed.title)
except AttributeError:
    print("Feed metadata is not available.")
    
    
    