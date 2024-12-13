from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:perfume_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart, name='cart'),
]
