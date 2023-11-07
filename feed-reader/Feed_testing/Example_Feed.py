import feedparser

# URL
feed_url = "https://github.com/acryldata/datahub-helm/releases.atom"

# Parse the feed
feed = feedparser.parse(feed_url)

try:
    print("Feed Title:", feed.feed.title)
    print("Feed Description:", feed.feed.description)
    print("Feed Link:", feed.feed.link)
except AttributeError:
    print("Feed metadata is not available.")

for entry in feed.entries:
    try:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Summary:", entry.summary)
        print("Published Date:", entry.published)
        print("\n")
    except AttributeError:
        print("Entry metadata is not available.")
        
