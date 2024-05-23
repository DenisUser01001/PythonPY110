from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from datetime import datetime
import requests


DIRECTION_TRANSFORM = {
    'N': 'северное',
    'NNE': 'северо - северо - восточное',
    'NE': 'северо - восточное',
    'ENE': 'восточно - северо - восточное',
    'E': 'восточное',
    'ESE': 'восточно - юго - восточное',
    'SE': 'юго - восточное',
    'SSE': 'юго - юго - восточное',
    'S': 'южное',
    'SSW': 'юго - юго - западное',
    'SW': 'юго - западное',
    'WSW': 'западно - юго - западное',
    'W': 'западное',
    'WNW': 'западно - северо - западное',
    'NW': 'северо - западное',
    'NNW': 'северо - северо - западное',
    'C': 'штиль',
}


def current_weather(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        """
        Получение данных с https://www.weatherapi.com/ (TRIAL Ends on 21/May/2024)
        """
        token = '5dd2c8c23e2f44b7a18222527240705'
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        if lat and lon:
            url = f"https://api.weatherapi.com/v1/current.json?key={token}&q={lat},{lon}"
            response = requests.get(url)
            data = response.json()
        else:
            lat = 59.93
            lon = 30.31
            url = f"https://api.weatherapi.com/v1/current.json?key={token}&q={lat},{lon}"
            response = requests.get(url)
            data = response.json()
        result = {
        'city': data['location']['name'],
        'time': data['location']['localtime'],
        'temp': data['current']['temp_c'],
        'feels_like_temp': data['current']['feelslike_c'],
        'pressure': data['current']['pressure_mb'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph'],
        'wind_gust': data['current']['gust_kph'],
        'wind_dir': DIRECTION_TRANSFORM.get(data['current']['wind_dir']),
        }
        return JsonResponse(result, json_dumps_params={'ensure_ascii': False,
                                                       'indent': 4})