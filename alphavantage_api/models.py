from django.db import models


# Create your models here.
class CurrencyRate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    exchange_rate = models.FloatField(default=0)
    bid_price = models.FloatField(default=0)
    ask_price = models.FloatField(default=0)
    last_refreshed = models.DateTimeField(null=True)

    class Meta:
        ordering = ["id"]
