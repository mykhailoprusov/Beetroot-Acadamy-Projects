import requests

print('Type the name of the city and get its weather')

city_name = input('Enter the name of the city ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=95f231c4a7a0ad6e64dbccb614ab6aa7'
weather_data = requests.get(url)



formatting = weather_data.json()
print(formatting)

print(f'Weather: {formatting["weather"][0]["description"]} , Temperature:{formatting["main"]["temp"]} ')