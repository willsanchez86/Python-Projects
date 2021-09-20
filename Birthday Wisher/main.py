##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = '*******'
PASSWORD = '**********'

TODAY = dt.date.today()
CURRENT_MONTH = TODAY.month
CURRENT_DAY = TODAY.day

# 1. Update the birthdays.csv
# birthdays = {
#     'Name':['Will Sanchez', 'Gabby Sanchez'],
#     'Email':['willsanchez86@gmail.com', 'gabbynsanchez@gmail.com'],
#     'Year':[1990,1997],
#     'Month':[9, 4],
#     'Day':[14, 10],
# }
#
# df_birthdays = pd.DataFrame(birthdays)


# df_birthdays.to_csv('birthdays.csv', mode='w', index=False)

df = pd.read_csv('birthdays.csv')
dict = df.to_dict(orient='records')

letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
for record in dict:
    # 2. Check if today matches a birthday in the birthdays.csv
    if record['Month'] == CURRENT_MONTH and record['Day'] == CURRENT_DAY:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(random.choice(letters), 'r') as file:
            greetings = file.read()
            updated_greetings = greetings.replace('[NAME]', record['Name'])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=record['Email'],
                msg=f'Subject:Feliz Cumpleanos!\n\n{updated_greetings}'
            )
    else:
        pass


