import requests

KEY = "5dd2c8c23e2f44b7a18222527240705"  # Получен при регистрации на сайте https://www.weatherapi.com/
LAT = "59.93"  # широта в градусах для Санкт-Петербурга
LON = "30.31"  # долгота в градусах для Санкт-Петербурга

YA_API_KEY = "c2e5a681-4b13-4708-93d6-3c06ec79c255"

url = f"https://api.weatherapi.com/v1/current.json?key={KEY}&q={LAT},{LON}"

response = requests.get(url)
print("Запрос через Weather API:")
print(response)
print(response.json())

url = f"https://api.weather.yandex.ru/v2/forecast?lat={LAT}&lon={LON}"
headers={"X-Yandex-API-Key": f"{YA_API_KEY}"}

response = requests.get(url, headers=headers)
print("Запрос через Яндекс API:")
print(response.json())
