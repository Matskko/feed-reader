import os
import smtplib
import feedparser
from datetime import datetime, timedelta
import pytz

# Importeer de benodigde modules

def check_feed_updates(feed_url, interval):
    """
    Controleer op updates in een opgegeven feed URL binnen een opgegeven tijdsinterval.

    Args:
        feed_url (str): De URL van de feed om updates te controleren.
        interval (int): Het aantal dagen om terug te kijken voor updates.

    Returns:
        list: Een lijst van dictionaries met informatie over de bijgewerkte items.
            Elke dictionary bevat de volgende sleutels:
            - 'update_date': De datum en tijd van de update in het formaat "%Y-%m-%d %H:%M:%S".
            - 'title': De titel van het bijgewerkte item.
            - 'summary': De samenvatting van het bijgewerkte item.
            - 'link': De link naar het bijgewerkte item.
    """
    feed = feedparser.parse(feed_url)

    current_date = datetime.now(pytz.utc)
    start_date = current_date - timedelta(days=interval)

    info = []

    for entry in feed.entries:
        entry_info = {}

        if 'published' in entry:
            entry_date = datetime.fromisoformat(entry.published)
        elif 'updated' in entry:
            entry_date = datetime.fromisoformat(entry.updated)
        else:
            print("Datum/tijdstempel niet gevonden voor deze entry.")
            continue

        entry_date = entry_date.replace(tzinfo=pytz.utc)
        if entry_date >= start_date:
            entry_info['update_date'] = entry_date.strftime("%Y-%m-%d %H:%M:%S")
            entry_info['title'] = entry.title
            entry_info['summary'] = entry.summary
            entry_info['link'] = entry.link

            info.append(entry_info)

    return info

def get_urls():
    # Lijst van feed URLs om te controleren
    urls = [
        'https://github.com/acryldata/datahub-helm/releases.atom',
        'http://github.com/datahub-project/datahub/releases.atom'
    ]
    return urls

def send_email(subject, message):
    FROM_EMAIL = os.getenv("YOUR_EMAIL")
    PASSWORD = os.getenv("YOUR_PASSWORD")
    TO_EMAIL = "tobiasvdvaart@gmail.com"  

    if FROM_EMAIL is None or PASSWORD is None:
        print("E-mailgegevens niet gevonden in omgevingsvariabelen.")
        return

    SMTP_SERVER = "smtp.office365.com"
    SMTP_PORT = 587

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(FROM_EMAIL, PASSWORD)

        msg = f"Subject: {subject}\n\n{message}".encode('utf-8')

        smtp.sendmail(FROM_EMAIL, TO_EMAIL, msg)

if __name__ == "__main__":
    # Haal het tijdsinterval op uit de omgevingsvariabele INTERVAL_IN_DAYS, standaard is 11 dagen
    interval = int(os.getenv("INTERVAL_IN_DAYS", default="11"))
    feed_urls = get_urls()

    all_feed_updates = []

    for feed_url in feed_urls:
        # Controleer op updates in elke feed URL
        feed_updates = check_feed_updates(feed_url, interval)
        all_feed_updates.extend(feed_updates)

    email_subject = "Feed Updates"
    email_body = "Lijst met updates:\n\n"

    for update in all_feed_updates:
        # Bouw de e-mailinhoud op met informatie over de updates
        email_body += f"Update gevonden op {update['update_date']}\n"
        email_body += f"Titel: {update['title']}\n"
        email_body += f"Samenvatting: {update['summary']}\n"
        email_body += f"Link: {update['link']}\n\n"
        
    send_email(email_subject, email_body)
    print("De e-mail is verstuurd.")

print("completed")