from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)
