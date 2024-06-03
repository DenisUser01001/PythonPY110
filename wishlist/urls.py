from django.urls import path

from wishlist.views import wishlist_view

#  TODO Импортируйте ваше представление

app_name = 'wishlist'

urlpatterns = [
        path('wishlist/', wishlist_view, name="wishlist_view"),
        path('wishlist/remove/<str:id_product>', wishlilst_remove_view, name="remove_now"),
]
