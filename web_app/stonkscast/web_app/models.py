from django.db import models

# Create your models here.
class Inference(models.Model):
    stock_name = models.CharField(max_length=20)
    market = models.CharField(max_length=20)
    kgv = models.FloatField()
    score = models.FloatField()