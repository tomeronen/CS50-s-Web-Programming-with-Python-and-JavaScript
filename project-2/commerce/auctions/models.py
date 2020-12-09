from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.management import get_contenttypes_and_models
from django.db import models


class User(AbstractUser):
    # add many to many
    pass


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image_src = models.CharField(max_length=200)
    current_price = models.IntegerField()


class Bid(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pass


class Comment(models.Model):
    content = models.CharField(max_length=500)
