# Amazon-Price-Tracker
This Python script monitors the price of an Instant Pot on a static website. It fetches the page with requests, extracts the price using BeautifulSoup, and checks every day at 9 AM if it’s below $100. If true, it sends an email with the price and link. Note: The site is static; the price does not actually change.

Amazon Price Tracker (Instant Pot)

This Python script monitors the price of an Instant Pot on a static website and sends an email if the price drops below $100.

Features

Fetches the webpage using requests.

Extracts the price using BeautifulSoup.

Checks daily at 9 AM if the price is below $100.

Sends an email with price and link via SMTP.

Uses environment variables for email and password.

Installation

Install Python 3

Install required packages:

pip install requests beautifulsoup4


Set environment variables:

Windows (PowerShell)

setx EMAIL "your_email@gmail.com"
setx EMAIL_PASSWORD "your_app_password"


Or: In PyCharm → Run Configuration → Environment Variables.

Usage

Run the script:

python main.py


The script checks the price and sends an email if conditions are met.

Important Note

The monitored site is static → the price on the example page does not change.

This is a demo script for web scraping and email notifications.
