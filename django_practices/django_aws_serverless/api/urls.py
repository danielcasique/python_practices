from django.urls import path
from .views import *

urlpatterns = [
    path('v1/dummy', Dummy.as_view()), 
]