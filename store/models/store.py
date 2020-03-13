import os

from django.contrib.auth.models import User
from django.db import models

from garden.models import Flower


class Store(models.Model):
    """
    Model for Store
    """

    store_name = models.CharField(max_length=200, null=False, blank=False)
    is_online = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name='owner')
    # TODO longitude
    # TODO latitude

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = "Store"
