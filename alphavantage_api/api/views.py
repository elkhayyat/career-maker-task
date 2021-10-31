from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import CurrencyRateSerializer
from alphavantage_api.tasks import get_data_from_api
from alphavantage_api.models import CurrencyRate
from alphavantage_api.tasks import get_data_from_api


# get last saved rate from DB
def get_last_rate():
    last_rate = CurrencyRate.objects.last()

    # if there is no saved rates at DB run the task
    if not last_rate:
        last_rate = get_data_from_api()

    # serializer the data and return it
    serializer = CurrencyRateSerializer(last_rate)
    return serializer


class CurrencyRateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        last_rate = get_last_rate()
        return Response(last_rate.data)

    def post(self, request, format=None):
        # force request the price from the api then retrieve it from DB
        get_data_from_api()
        last_rate = get_last_rate()
        return Response(last_rate.data)
