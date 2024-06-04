from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user

from logic.services import view_in_wishlist, add_to_wishlist, remove_from_wishlist
from store.models import DATABASE


def wishlist_view(request: HttpRequest):
    if request.method == "GET":
        if request.method == "GET":

            current_user = get_user(request).username
            data = view_in_wishlist(request)[current_user]

            products = []
            for product_id in data['products']:
                product = DATABASE[product_id]
                products.append(product)

            return render(request, "wishlist/wishlist.html", context={"products": products})


def wishlist_add_json(request, id_product: str):
    """
    Добавление продукта в избранное и возвращение информации об успехе или неудаче в JSON
    """
    if request.method == "GET":
        result = add_to_wishlist(request, id_product)  # вызов обработчик из services.py добавляющий продукт в избранное
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в избранное"},
                                json_dumps_params={'ensure_ascii': False})  # JsonResponse с ключом "answer" и значением "Продукт успешно добавлен в избранное"

        return JsonResponse({"answer": "Неудачное добавление в избранное"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})  # JsonResponse с ключом "answer" и значением "Неудачное добавление в избранное" и параметром status=404


def wishlist_del_json(request, id_product: str):
    """
    Удаление продукта из избранного и возвращение информации об успехе или неудаче в JSON
    """
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product)  # обработчик из services.py удаляющий продукт из избранного
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из избранного"},
                                json_dumps_params={'ensure_ascii': False})  # JsonResponse с ключом "answer" и значением "Продукт успешно удалён из избранного"

        return JsonResponse({"answer": "Неудачное удаление из избранного"},
                            json_dumps_params={'ensure_ascii': False})  # JsonResponse с ключом "answer" и значением "Неудачное удаление из избранного" и параметром status=404


def wishlist_json(request):
    """
    Просмотр всех продуктов в избранном для пользователя и возвращение этого в JSON
    """
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(request)[current_user]  # данные о списке товаров в избранном у пользователя
        if data:
            return JsonResponse(data,
                                json_dumps_params={'ensure_ascii': False, 'indent': 4})  # JsonResponse c data

        return JsonResponse({"answer": "Пользователь не авторизирован"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})  # JsonResponse с ключом "answer" и значением "Пользователь не авторизирован" и параметром status=404