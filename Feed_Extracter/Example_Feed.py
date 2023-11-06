import feedparser

# Specify the URL of the feed you want to parse
feed_url = "https://example.com/feed.rss"

# Parse the feed
feed = feedparser.parse(feed_url)

try:
    # Check for feed-level information
    print("Feed Title:", feed.feed.title)
    print("Feed Description:", feed.feed.description)
    print("Feed Link:", feed.feed.link)
except AttributeError:
    print("Feed metadata is not available.")

# Iterate through entries in the feed
for entry in feed.entries:
    try:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Summary:", entry.summary)
        print("Published Date:", entry.published)
        print("\n")
    except AttributeError:
        print("Entry metadata is not available.")
        
