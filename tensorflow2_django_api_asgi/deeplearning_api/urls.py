from django.urls import path
from .views import *

urlpatterns = [
    path('api/predict', predict),
    path('', healthcheck),
]