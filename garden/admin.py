from django.contrib import admin
from garden.models import Category, Flower


class CategoryAdmin(admin.ModelAdmin):
    fields = ('tag', 'description')   

class FlowerAdmin(admin.ModelAdmin):
    fields = ('name', 'category', 'info')   



admin.site.register(Category, CategoryAdmin)
admin.site.register(Flower, FlowerAdmin)
