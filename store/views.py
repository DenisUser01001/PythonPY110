from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseNotFound
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

from store.models import DATABASE
from logic.services import filtering_category, add_to_cart, remove_from_cart, view_in_cart


def products_view(request):
    if request.method == "GET":
        # Обработка id из параметров запроса (уже было реализовано ранее)
        id_product = request.GET.get('id')
        if id_product is None:
            category_key = request.GET.get('category')
            ordering_key = request.GET.get('ordering')

            if ordering_key:
                if request.GET.get('reverse') and request.GET.get('reverse').lower() == 'true':
                    data = filtering_category(DATABASE, category_key, ordering_key, True)
                else:
                    data = filtering_category(DATABASE, category_key, ordering_key)
            else:
                data = filtering_category(DATABASE, category_key)

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
                    same_category = filtering_category(DATABASE, category_key=data['category'])
                    same_category.remove(data)
                    same_category = same_category[:5]
                    return render(request, "store/product.html", context={"product": data, "same_category": same_category})

        elif isinstance(page, int):
            # Обрабатываем условие того, что пытаемся получить страницу товара по его id
            data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if data:
                same_category = filtering_category(DATABASE, category_key=data['category'])
                same_category.remove(data)
                same_category = same_category[:5]
                return render(request, "store/product.html", context={"product": data, "same_category": same_category})
        return HttpResponse(status=404)


def shop_view(request: HttpRequest):
    if request.method == "GET":
        category_key = request.GET.get("category")  # Обработка фильтрации из параметров запроса
        ordering_key = request.GET.get("ordering")
        reverse_key = request.GET.get("reverse")
        if ordering_key:
            if reverse_key and reverse_key.lower() == 'true':
                data = filtering_category(DATABASE, category_key, ordering_key, True)
            else:
                data = filtering_category(DATABASE, category_key, ordering_key)
        else:
            data = filtering_category(DATABASE, category_key)

        return render(request, 'store/shop.html', context={"products": data, "category": category_key})  #в представлени shop_view в словарь передадим какую категорию выбрали для фильтрации


@login_required(login_url='login:login_view')
def cart_view(request: HttpRequest):
    if request.method == "GET":

        current_user = get_user(request).username
        data = view_in_cart(request)[current_user]

        json_param = request.GET.get("format")
        if json_param and json_param.lower() == "json":
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})

        products = []
        for product_id, quantity in data['products'].items():
            product = DATABASE[product_id]
            product['quantity'] = quantity
            product['price_total'] = f"{quantity * product['price_after']:.2f}"
            products.append(product)
        return render(request, "store/cart.html", context={"products": products})


@login_required(login_url='login:login_view')
def cart_add_view(request: HttpRequest, id_product):
    if request.method == "GET":
        result = add_to_cart(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request: HttpRequest, id_product):
    if request.method == "GET":
        result = remove_from_cart(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


@login_required(login_url='login:login_view')
def cart_buy_now_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(request, id_product)
        if result:
            return redirect("store:cart_view")
        return HttpResponseNotFound("Неудачное добавление в корзину")


def cart_remove_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(request, id_product)
        if result:
            return redirect("store:cart_view")

        return HttpResponseNotFound("Неудачное удаление из корзины")


def coupon_check_view(request, name_coupon):
    # DATA_COUPON - база данных купонов: ключ - код купона (name_coupon);
    # значение - словарь со значением скидки в процентах и
    # значением действителен ли купон или нет
    DATA_COUPON = {
        "coupon": {
            "value": 10,
            "is_valid": True},
        "coupon_old": {
            "value": 20,
            "is_valid": False},
    }
    if request.method == "GET":
        if name_coupon and name_coupon in DATA_COUPON:
            return JsonResponse({'discount': DATA_COUPON[name_coupon]['value'], 'is_valid': DATA_COUPON[name_coupon]['is_valid']})
        return HttpResponse('Неверный купон.')
        # Проверьте, что купон есть в DATA_COUPON, если он есть, то верните JsonResponse в котором по ключу "discount"
        # получают значение скидки в процентах, а по ключу "is_valid" понимают действителен ли купон,
        # или нет (True, False)
        # Если купона нет в базе, то верните HttpResponseNotFound("Неверный купон")


def delivery_estimate_view(request):
    # База данных по стоимости доставки.
    # Ключ - Страна; Значение словарь с городами и ценами; Значение с ключом fix_price
    # применяется если нет города в данной стране.
    DATA_PRICE = {
        "Россия": {
            "Москва": {"price": 80},
            "Санкт-Петербург": {"price": 80},
            "fix_price": 100,
        },
    }
    if request.method == "GET":
        data = request.GET
        country = data.get('country')
        city = data.get('city')
        if country in DATA_PRICE and city in DATA_PRICE[country]:
            return JsonResponse({'price': DATA_PRICE[country][city]['price']})
        elif country in DATA_PRICE and city not in DATA_PRICE[country]:
            return JsonResponse({'price': DATA_PRICE[country]['fix_price']})
        return HttpResponseNotFound("Неверные данные")
        # Реализуйте логику расчёта стоимости доставки, которая выполняет следующее:
        # Если в базе DATA_PRICE есть и страна (country) и существует город(city),
        # то вернуть JsonResponse со словарём, {"price": значение стоимости доставки}
        # Если в базе DATA_PRICE есть страна, но нет города,
        # то вернуть JsonResponse со словарём, {"price": значение фиксированной стоимости доставки}
        # Если нет страны, то вернуть HttpResponseNotFound("Неверные данные")
