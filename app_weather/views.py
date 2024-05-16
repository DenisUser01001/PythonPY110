from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

from datetime import datetime
import requests

# Create your views here.

# Словарь перевода значений направления ветра
# DIRECTION_TRANSFORM = {
#     'n': 'северное',
#     'nne': 'северо - северо - восточное',
#     'ne': 'северо - восточное',
#     'ene': 'восточно - северо - восточное',
#     'e': 'восточное',
#     'ese': 'восточно - юго - восточное',
#     'se': 'юго - восточное',
#     'sse': 'юго - юго - восточное',
#     's': 'южное',
#     'ssw': 'юго - юго - западное',
#     'sw': 'юго - западное',
#     'wsw': 'западно - юго - западное',
#     'w': 'западное',
#     'wnw': 'западно - северо - западное',
#     'nw': 'северо - западное',
#     'nnw': 'северо - северо - западное',
#     'c': 'штиль',
# }
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


def current_weather(request: HttpRequest, lat=59.93, lon=30.31) -> JsonResponse:
    if request.method == "GET":
        """
        Получение данных с https://www.weatherapi.com/ (TRIAL Ends on 21/May/2024)
        """
        token = '5dd2c8c23e2f44b7a18222527240705'
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
        # """
        # Описание функции, входных и выходных переменных
        # """
        # token = 'c2e5a681-4b13-4708-93d6-3c06ec79c255'  # Вставить ваш токен
        # url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"  # Если вдруг используете тариф «Погода на вашем сайте»
        # # то вместо forecast используйте informers. url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}"
        # headers = {"X-Yandex-API-Key": f"{token}"}
        # response = requests.get(url, headers=headers)
        # data = response.json()
        #
        # # Данная реализация приведена для тарифа «Тестовый», если у вас Тариф «Погода на вашем сайте», то закомментируйте пару строк указанных ниже
        # result = {
        #     'city': data['geo_object']['locality']['name'],  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        #     'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        #     'temp': data['fact']['temp'],  # TODO Реализовать вычисление температуры из данных полученных от API
        #     'feels_like_temp': data['fact']['feels_like'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
        #     'pressure': data['fact']['pressure_mm'],  # TODO Реализовать вычисление давления из данных полученных от API
        #     'humidity': data['fact']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
        #     'wind_speed': data['fact']['wind_speed'],  # TODO Реализовать вычисление скорости ветра из данных полученных от API
        #     'wind_gust': data['fact']['wind_gust'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
        #     'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        # }
        return JsonResponse(result, json_dumps_params={'ensure_ascii': False,
                                                       'indent': 4})
