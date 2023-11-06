import os
import feedparser
from datetime import datetime, timedelta
import pytz

# Definieer een functie om de feeds te controleren en updates weer te geven
def check_feed_updates(feed_url, interval):
    feed = feedparser.parse(feed_url)


    current_date = datetime.now(pytz.utc)  # Gebruik UTC-tijdzone
    start_date = current_date - timedelta(days=interval)

    for entry in feed.entries:
        # Probeer 'published', als dat niet beschikbaar is, probeer 'updated'
        if 'published' in entry:
            entry_date = datetime.fromisoformat(entry.published)
        elif 'updated' in entry:
            entry_date = datetime.fromisoformat(entry.updated)
        else:
            print("Datum/tijdstempel niet gevonden voor deze entry.")
            continue

        entry_date = entry_date.replace(tzinfo=pytz.utc)  # Zorg ervoor dat het datetime-object in UTC is
        if entry_date >= start_date:
            print("Update found on", entry_date.strftime("%Y-%m-%d %H:%M:%S"))
            print("Title:", entry.title)
            print("Summary:", entry.summary)
            print("Link:", entry.link)
            print("\n")


# Hier wordt de lijst met feed-URL's gedefinieerd
def get_urls():
    urls = [
        'https://github.com/acryldata/datahub-helm/releases.atom',
        'http://github.com/datahub-project/datahub/releases.atom'
    ]
    return urls

# Hier wordt het interval in dagen gedefinieerd
interval = int(os.getenv("INTERVAL_IN_DAYS", default="3"))

# Hierdoor worden updates gecontroleerd voor elke feed in de lijst
feed_urls = get_urls()
for feed_url in feed_urls:
    check_feed_updates(feed_url, interval)
    
