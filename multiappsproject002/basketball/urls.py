from django.urls import path
from . import views

urlpatterns = [
    path("basketball/", views.Basket_Info), 
]


 
