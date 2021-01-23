from django.urls import path
from .views import *

urlpatterns = [
    path('api/predict', PredictAPI.as_view()),
    path('', HealthCheck.as_view()),
]