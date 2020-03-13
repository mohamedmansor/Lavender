import os

from django.db import models

from garden.models import Category
from store.models import Store


class Flower(models.Model):
    """
    Model for Flower
    """

    def get_image_path(self, filename):
        return os.path.join('photos', str(self.name), filename)

    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False, related_name='category')
    stores = models.ManyToManyField(Store, on_delete=models.PROTECT, null=False, blank=True, related_name='stores')
    picture = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    info = models.TextField(null=True, blank=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Garden'
        verbose_name_plural = "Garden"
