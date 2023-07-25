#APP aplicación denominada disqueraLC
from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name= "inicio"),
]