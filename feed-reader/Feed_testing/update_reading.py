import os

def get_interval():
    interval = int(os.getenv("INTERVAL_IN_DAYS", default="14"))
    return interval

def get_urls():
    urls = [
        'https://github.com/acryldata/datahub-helm/releases.atom',
        'http://github.com/datahub-project/datahub/releases.atom'
    ]
    return urls

# Gebruik de get_interval-functie om de waarde van interval in te stellen
interval = get_interval()


