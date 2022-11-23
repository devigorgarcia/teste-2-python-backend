import uuid

from django.db import models
from django.forms import UUIDField
from traitlets import default


# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    card = models.CharField(max_length=20)
    hour = models.CharField(max_length=20)
    shop_owner = models.CharField(max_length=20)
    shop_name = models.CharField(max_length=20)
