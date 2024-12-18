from django.urls import path
from . import views

urlpatterns = [
    path('', views.finalise_purchase, name='finalise_purchase'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
