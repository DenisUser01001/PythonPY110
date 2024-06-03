from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect


def wishlist_view(request: HttpRequest):
    if request.method == "GET":
        if request.method == "GET":

            # current_user = get_user(request).username
            # data = view_in_wishlist(request)[current_user]

            # products = []
            # for product_id, quantity in data['products'].items():
            #     product = DATABASE[product_id]
            #     product['quantity'] = quantity
            #     product['price_total'] = f"{quantity * product['price_after']:.2f}"
            #     products.append(product)

            return render(request, "wishlist/wishlist.html")
