import requests

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        endpoint = 'https://api.sheety.co/0911b0d267ba5a15508f9429d802e2bd/cheapFlightFinder/sheet1'
        response = requests.get(url=endpoint)
        data = response.json()
        self.destination_data = data['sheet1']
        return self.destination_data

    def update_city_id(self):
        for row in self.destination_data:
            new_data ={
                'sheet1': {
                    'cityId': row['cityId']
                }
            }
            response = requests.put(url=f'https://api.sheety.co/0911b0d267ba5a15508f9429d802e2bd/cheapFlightFinder/sheet1/{row["id"]}', json=new_data)
            print(response.text)