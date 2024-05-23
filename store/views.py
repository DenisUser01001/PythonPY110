from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseNotFound
import requests

from store.models import DATABASE
from logic.services import filtering_category

# Create your views here.


def products_view(request: HttpRequest):
    if request.method == "GET":

        prod_id = request.GET.get('id')
        products_id_in_database = []
        for temp1, temp2 in DATABASE.items():
            products_id_in_database.append(temp2['id'])

        if prod_id in products_id_in_database:
            for key, nested_dict in DATABASE.items():
                if nested_dict['id'] == int(prod_id):

                    # Добавление сортировки:

                    #
                    return JsonResponse(nested_dict, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        elif prod_id is None:
            return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        else:
            return HttpResponseNotFound("<h1>Данного продукта нет в базе данных</h1>")


def products_page_view(request: HttpRequest, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:
                    with open(f'store/products/{data['html']}.html', 'r', encoding="utf-8") as f:
                        return HttpResponse(f.read())

        elif isinstance(page, int):
            if str(page) in DATABASE:
                with open(f'store/products/{DATABASE[str(page)]["html"]}.html', 'r', encoding="utf-8") as f:
                    return HttpResponse(f.read())

        return HttpResponse(status=404)






def shop_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()
            return HttpResponse(data)
