import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
print(scraper.get("https://www.wootware.co.za/computer-hardware/video-cards-video-devices/shopby/in_stock_with_wootware?dir=asc&order=price").text)  # => "<!DOCTYPE html><html><head>..."
