from django.urls import include, path
from rest_framework import routers
from alphavantage_api.api import views

urlpatterns = [
    # urls for Django Rest Framework API
    path('quotes', views.CurrencyRateView.as_view(), name='BTC2USD'),
]