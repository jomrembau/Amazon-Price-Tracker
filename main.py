from bs4 import BeautifulSoup
import requests
import smtplib
import datetime as dt
import os

email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PASSWORD")

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL, headers={"Accept-Language":"en-US"})
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "html.parser")

whole_price = soup.find("span", class_ = "a-price-whole")
fraction_price = soup.find("span", class_ = "a-price-fraction")

current_price = f"{whole_price.text}{fraction_price.text}"
current_price = float(current_price)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
now = dt.datetime.now()

message = (f"Subject: Time to buy!  \n\n"
           f" Instant Pot is now priced at ${current_price} \n\n"
           f" Link to buy: {URL}")

connection.login(user=email,password= password)
if now.hour == 9 and current_price < 100.00:
    connection.sendmail(from_addr=email,
                        to_addrs="jomir.bautista@gmail.com",
                        msg= message.encode("utf-8"))

connection.close()


