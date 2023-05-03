from django.urls import path
from . import views

urlpatterns = [
    path("football/", views.Football_Info), 
]


 
