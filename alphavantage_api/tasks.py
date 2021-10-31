from alphavantage_api.models import CurrencyRate
import os
import requests
from celery import shared_task


@shared_task
def get_data_from_api(*args, **kwargs):
    # GET API KEY from setting which loaded from .env
    api_key = os.environ.get('ALPHAVANTAGE_API_KEY')

    # alphavantage API
    url = "https://www.alphavantage.co/query"
    query_parameters = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "BTC",
        "to_currency": "USD",
        "apikey": api_key,
    }

    # fetch data from api
    response = requests.request(
        "GET", url, params=query_parameters
    ).json()

    # Save Data Into Postgres
    entry = CurrencyRate()
    entry.exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    entry.ask_price = response['Realtime Currency Exchange Rate']['9. Ask Price']
    entry.bid_price = response['Realtime Currency Exchange Rate']['8. Bid Price']
    entry.last_refreshed = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
    entry.save()

