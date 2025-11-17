# Amazon-Price-Tracker
This Python script monitors the price of an Instant Pot on a static website. It fetches the page with requests, extracts the price using BeautifulSoup, and checks every day at 9 AM if it’s below $100. If true, it sends an email with the price and link. Note: The site is static; the price does not actually change.
