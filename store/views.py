from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseNotFound
import requests

from store.models import DATABASE
from logic.services import filtering_category, add_to_cart, remove_from_cart, view_in_cart

# Create your views here.

"""Моя первая версия отображения продуктов в JSON и отдельного JSON продукта по id:"""
# def products_view(request: HttpRequest):
#     if request.method == "GET":
#         prod_id = request.GET.get('id')
#
#         products_id_in_database = []
#         for temp1, temp2 in DATABASE.items():
#             products_id_in_database.append(temp2['id'])
#
#         if prod_id in products_id_in_database:
#             for key, nested_dict in DATABASE.items():
#                 if nested_dict['id'] == int(prod_id):
#
#                     return JsonResponse(nested_dict, json_dumps_params={'ensure_ascii': False, 'indent': 4})
#         elif prod_id is None:
#             return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False, 'indent': 4})
#         else:
#             return HttpResponseNotFound("<h1>Данного продукта нет в базе данных!</h1>")

"""Версия, переписанная на основании практических пособий:"""


def products_view(request):
    if request.method == "GET":
        # Обработка id из параметров запроса (уже было реализовано ранее)
        id_product = request.GET.get('id')
        if id_product is None:
            category_key = request.GET.get('category')  # Считали 'category'
            ordering_key = request.GET.get('ordering')  # Считали в каком порядке будем сортировать

            if ordering_key:  # Если в параметрах есть 'ordering'
                if request.GET.get('reverse') and request.GET.get('reverse').lower() == 'true':  # Если в параметрах есть 'ordering' и 'reverse'=True
                    data = filtering_category(DATABASE, category_key, ordering_key, True)  # TODO Использовать filtering_category и провести фильтрацию с параметрами category, ordering, reverse=True
                else:  # Если не обнаружили в адресно строке ...&reverse=true , значит reverse=False
                    data = filtering_category(DATABASE, category_key, ordering_key)  # TODO Использовать filtering_category и провести фильтрацию с параметрами category, ordering, reverse=False
            else:
                data = filtering_category(DATABASE, category_key)  # TODO Использовать filtering_category и провести фильтрацию с параметрами category

            # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
            return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})

        else:
            data = DATABASE.get(id_product)
            if data:
                return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
            else:
                return HttpResponseNotFound("<h1>Данного продукта нет в базе данных!</h1>")


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
        return render(request, 'store/shop.html', context={"products": DATABASE.values()})
        # with open('store/shop.html', encoding="utf-8") as f:
        #     data = f.read()
        #     return HttpResponse(data)


def cart_view(request: HttpRequest):
    if request.method == "GET":
        data = view_in_cart()  # TODO Вызвать ответственную за это действие функцию
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


def cart_add_view(request: HttpRequest, id_product: int):
    if request.method == "GET":
        result = add_to_cart(id_product)  # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request: HttpRequest, id_product: int):
    if request.method == "GET":
        result = remove_from_cart(id_product)  # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})
