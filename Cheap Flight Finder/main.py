#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from datetime import date, timedelta
from data_manager import DataManager
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()
flight_search = FlightSearch()

if sheet_data[0]["cityId"] == "":
    for row in sheet_data:
        row['cityId'] = flight_search.get_city_id(row['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_city_id()

tomorrow = date.today() + timedelta(days=1)
six_months_from_today = (date.today() + timedelta(6 * 365 / 12))
AIRPORT_CODE = 'LAX'

for city in sheet_data:
    flight = flight_search.check_flights(
            origin_city_code=AIRPORT_CODE,
            destination_city_id=city['cityId'],
            date_from=tomorrow,
            date_to=six_months_from_today
        )

    if flight is not None and flight['price'] < city['lowestPrice']:
        notification_manager.send_sms(message=f"Low price alert! Only ${flight['price']} to fly from {flight['origin_city']}-{flight['origin_airport']} to {flight['destination_city']}-{flight['destination_airport']}, from {flight['out_date']} to {flight['return_date']}.")
