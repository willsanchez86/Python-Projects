import smtplib
import datetime as dt
import random

MY_EMAIL = '*********'
PASSWORD = '**************'

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.date(year=1990, month=9, day=14)



# if day_of_week == 3:
#     with open('quotes.txt', 'r') as file:
#         quotes = file.read()
#         quotes_list = quotes.split('\n')
#         msg = random.choice(quotes_list)
#     with smtplib.SMTP('smtp.gmail.com') as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs='rlmehling@gmail.com',
#             msg=f'Subject:Thursday Vibez\n\n{msg}'
#         )
