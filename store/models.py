import os

from django.db import models

from garden.models import Flower


class Store(models.Model):
    """
    Model for Store
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    is_online = models.BooleanField(default=False)
    # location TODO

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = "Store"
