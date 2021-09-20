import requests
from datetime import date,datetime


TODAY = date.today()
TIME = datetime.now().strftime("%H:%M:%S")


APP_ID = "3a7fe173"
API_Key = "**********"

BEARER_TOKEN = '**********'

exercise = input('Tell me what exercises you did: ')


workout_params = {
 "query": exercise,
 "gender":"male",
 "weight_kg":88.5,
 "height_cm":167.64,
 "age":30
}
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_Key,
    'x-remote-user-id': '0'
}
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=nutritionix_endpoint, json=workout_params, headers=headers)
results = response.json()
print(results)

sheet_inputs = {
    'sheet1': {
        'date': str(TODAY),
        'time': str(TIME),
        'exercise': results['exercises'][0]['name'],
        'duration': results['exercises'][0]['duration_min'],
        'calories': results['exercises'][0]['nf_calories']
    }
}
sheety_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
	"Content-Type": "application/json",
}
sheety_endpoint = 'https://api.sheety.co/****************/workoutTracker/sheet1'

post = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_header)
print(post.text)
