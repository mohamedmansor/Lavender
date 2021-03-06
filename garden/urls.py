"""lavender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

garden_router = DefaultRouter(trailing_slash=False)

garden_router.register(
    r'flowers', views.FlowersViewSet, base_name='flowers')
garden_router.register(
    r'categories', views.CategoriesViewSet, base_name='categories')

urlpatterns = [
    path('garden/', include(garden_router.urls))
]
