import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = 'runpyure@gmail.com'
PASSWORD = 'Newpickle10'

PRODUCT_URL = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'

headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
}

response = requests.get(url=PRODUCT_URL, headers=headers)
webpage = response.content

soup = BeautifulSoup(webpage, 'lxml')
price = soup.find(class_='a-spacing-none a-text-left a-size-mini twisterSwatchPrice').get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

target_price = 200
if price_as_float < target_price:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='willsanchez86@gmail.com',
            msg=f'HOT PRICE! Now only ${price_as_float}! Buy at https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'

        )