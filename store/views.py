from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest

from store.models import DATABASE

# Create your views here.


def products_view(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        # Вернуть JsonResponse с объектом DATABASE и параметрами отступов и кодировок,
        # как в приложении app_weather


def shop_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()
            return HttpResponse(data)
