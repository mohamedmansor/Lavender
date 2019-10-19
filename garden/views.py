from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import Category, Flower


class FlowersViewSet(viewsets.ModelViewSet):
    serializer_class = ""

    def get_queryset(self):
        flowers = Flower.objects.all()
        return flowers
    
    # @action(detail=True, methods=['POST'])
    # def add_flower():
