from django.db import models


class Category(models.Model):
    """
    Model for Flower type
    """
    tag = models.CharField(max_length=200, null=False, blank=False)
    category_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = "Categories"
