from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),
]
