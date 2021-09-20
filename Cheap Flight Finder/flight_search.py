import requests

LOCATION_QUERY_KEY = '241fmuIn473X9uovS85VRxICZ5BupvAS'
ENDPOINT = 'http://tequila-api.kiwi.com'
FLIGHT_SEARCH_KEY = '241fmuIn473X9uovS85VRxICZ5BupvAS'

class FlightSearch:

    def get_city_id(self, city_name):
        header = {'apikey': LOCATION_QUERY_KEY}
        query = {
            'term': city_name,
            'location_types': 'city'
        }
        response = requests.get(url=f'{ENDPOINT}/locations/query', params=query, headers=header)
        results = response.json()['locations']
        code = results[0]["id"]
        return code

    def check_flights(self, origin_city_code, destination_city_id, date_from, date_to):
        header = {
            'apikey': FLIGHT_SEARCH_KEY,
            'Content-Encoding': 'gzip,'
        }
        query = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_id,
            'date_from': str(date_from.strftime("%d/%m/%Y")),
            'date_to': str(date_to.strftime("%d/%m/%Y")),
            'nights_in_dst_from': 3,
            'nights_in_dst_to': 28,
            'one_for_city': 1,
            'max_stopovers': 0,
            'flight_type': 'round',
            'curr': 'USD',
        }

        response1 = requests.get(url=f'{ENDPOINT}/v2/search', headers=header, params=query)
        try:
            data = response1.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_id}.")
            return None

        flight_data = {
            'price': data['price'],
            'origin_city': data['cityFrom'],
            'origin_airport': data['flyFrom'],
            'destination_city': data['cityTo'],
            'destination_airport': data['flyTo'],
            'out_date': data['route'][0]['local_departure'].split('T')[0],
            'return_date': data['route'][1]['local_departure'].split('T')[0],
        }

        print(flight_data['destination_city'], flight_data['price'])
        return flight_data
