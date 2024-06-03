from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import get_user

from logic.services import view_in_wishlist
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
