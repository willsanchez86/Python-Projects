import requests
from datetime import date, timedelta
import math
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TODAY = date.today()
YESTERDAY = str(TODAY - timedelta(days=1))
PRIOR_DAY = str(TODAY - timedelta(days=2))

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': '************',
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
yesterday_close = float(data[YESTERDAY]['4. close'])
prior_day_close = float(data[PRIOR_DAY]['4. close'])

percent_change = math.floor(abs(yesterday_close - prior_day_close) / prior_day_close * 100)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


def get_news():
    parameters = {
    'apiKey': '***************',
    'q': COMPANY_NAME,
    }
    # X-Api-Key: 'b4708682559045a59a35b8332d33947e'
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()

    data = response.json()['articles'][0:3]

    for article in data:
        headline = article['title']
        brief = article['description']
        client = Client('*********', '*************')
        message = client.messages \
            .create(
            body=f'{STOCK}\nHeadline: {headline}\n Brief: {brief}',
            from_='+19892600339',
            to='+************'
        )
        print(message.status)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

if percent_change >= 5:
    get_news()


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

