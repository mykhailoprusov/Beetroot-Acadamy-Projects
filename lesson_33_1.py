import requests
import json


response = requests.get('https://en.wikipedia.org/robots.txt')

print(response.status_code)

data = response.text

with open('robots_data.json', 'w') as f:
    json.dump(data, f)