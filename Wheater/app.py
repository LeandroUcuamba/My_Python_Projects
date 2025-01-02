import requests

API_KEY = "955e1255e0ad6315bd81ec008657cbaa"
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occurred.")