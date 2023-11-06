import feedparser

# Specify the URL of the feed you want to parse
feed_url = "https://github.com/acryldata/datahub-helm/releases.atom"

# Parse the feed
feed = feedparser.parse(feed_url)

try:
    # Check for feed-level information
    print("Title:", feed.feed.title)
    print("Feed Link:", feed.feed.link)
    print("Feed Updated:", feed.feed.updated)
except AttributeError:
    print("Feed metadata is not available.")
    


def send_mail(recipients: list, subject: str, content: str):
    print(
        f"{subject=}"
        f"{recipients=}"
        f"{content=}"
    )

recipients = ["test@gmail.com"]
subject = "Dit is het onderwerp van de e-mail"
content = "Dit is de inhoud van de e-mail."

send_mail(recipients, subject, content)

