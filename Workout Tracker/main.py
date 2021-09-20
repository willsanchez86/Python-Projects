import json
from bs4 import BeautifulSoup
import requests
import re

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, 'html.parser')



movie = soup.find(string=re.compile("titleText", re.IGNORECASE))
print(movie)
# movies_list = [movie.getText() for movie in soup.find_all(name='h3', class_='jsx-4245974604')]
# print(movies_list)
