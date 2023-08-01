from django.db import models
from django.contrib.auth import get_user_model


class Instrument(models.Model):
    store_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    instrument = models.CharField(max_length=255)
    model =  models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    desc = models.TextField()


    def __str__(self):
        return self.instrument