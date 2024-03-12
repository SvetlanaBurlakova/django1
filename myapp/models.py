from django.db import models

# Create your models here.

class CoinFlip(models.Model):
    CHOICES = (('H', 'head'), ('T', 'tail'))
    side = models.CharField(choices=CHOICES, max_length=1)
    datetime = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_fields(n: int):
        result = CoinFlip.objects.order_by('-datetime')
        return result[:n]

    def __str__(self):
        return f'{self.side}: {self.datetime}'