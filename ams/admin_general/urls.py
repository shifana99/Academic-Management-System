from django.urls import path
from .import views

urlpatterns = [
     path('ind/',views.index),
]