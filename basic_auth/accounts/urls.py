from django.urls import path
from .views import register,welcome


urlpatterns = [
    path('',welcome),
    path('register/',register, name='register'),
]

