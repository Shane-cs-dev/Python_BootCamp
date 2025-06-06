import json
from pyexpat.errors import messages

from twilio.rest import Client
import requests
#########################################
DATE = 2024-12-28
#########################################
STOCK_API_KEY = "WJKEW3WF7V8QDF3R"
STOCK_URL = "https://www.alphavantage.co/query"
stock_param = {
    "apikey": STOCK_API_KEY,
    "symbol": "KLAC",
    "interval":"60min",
    "function": "TIME_SERIES_DAILY"
}
#########################################
NEWS_API_KEY = "ebbef8ea419a4df7b9477c74320b8c8d"
NEWS_URL = "https://newsapi.org/v2/everything"
news_param = {
    "q": "KLAC",
    "from": DATE,
    "to": DATE,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY

}
#########################################
TWILIO_API_KEY = "c72378ff1b3ba3f0bdc611b52ac8d62e"
ACCOUNT_SID = "ACf1f38f0cb0424eb2b2b2563d35f492da"
AUTH_TOKEN = "39e6877bc1706061c516fb5ee8fb136f"
###############Stock price practice##########################
# with open(file="./data.json", mode="r") as stock_json:
#     stock_data = json.load(stock_json)
#     new_stock_data = stock_data["Time Series (Daily)"]
#     new_stock_data2 = [value for (key, value) in new_stock_data.items()]
#     yesterday_price = new_stock_data2[0]["4. close"]
#     day_before_yesterday_price = new_stock_data2[1]["4. close"]
# print(yesterday_price)
# print(day_before_yesterday_price)
# stock_price_difference = abs(float(yesterday_price) - float(day_before_yesterday_price))
# difference_percentage = round(stock_price_difference/float(yesterday_price) *100, 3)
# print(stock_price_difference)
# print(difference_percentage)
###############Stock price##########################
response_stock = requests.get(url=STOCK_URL, params=stock_param)
response_stock.raise_for_status()
stock_data = response_stock.json()
# print(stock_data)
new_stock_data = stock_data["Time Series (Daily)"]
# print(new_stock_data)
new_stock_list = [value for (key, value) in new_stock_data.items()]
# print(new_stock_list)
yesterday_price = new_stock_list[0]["4. close"]
# print(yesterday_price)
day_before_yesterday_price = new_stock_list[1]["4. close"]
price_difference = abs(float(yesterday_price) - float(day_before_yesterday_price))
difference_percentage = round((price_difference/float(yesterday_price)) *100, 3)
# print(difference_percentage)
#Define price up or down
up_down = None
if float(yesterday_price) - float(day_before_yesterday_price) > 0:
    up_down = "🔼"
else:
    up_down = "🔻"
###############Stock News##########################
response_news = requests.get(url=NEWS_URL, params=news_param)
response_news.raise_for_status()
news_data = response_news.json()
# print(news_data["articles"][:3])
top_news = news_data["articles"][:3]
# print(top_news)
practice = [f"KLAC: {difference_percentage}%{up_down}\nHeadline: {value['title']}\nBrief: {value['description']}" for value in top_news]
# print(practice)
# for article in practice:
#     print(article)
#################################################
if_warning = False
if difference_percentage > 0.4:
    if_warning = True


if if_warning:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in practice:
        print(article)
        message = client.messages.create(
            body= article,
            from_="+19783500258",
            to="+886965315213",
        )
        print(message.status)

