from django.urls import path

from . import views

urlpatterns = [
    path('primera', views.primera, name='primera'),
]