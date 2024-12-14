from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:perfume_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart, name='cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
