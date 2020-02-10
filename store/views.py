import json

from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from store.models import Store
from store.serializers import StoreSerializer


class StoreViewSet(viewsets.ViewSet):
    serializer_class = StoreSerializer

    def list(self, request):
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=200)

    def create(self, request):
        serializer = StoreSerializer(data=self.request.data)
        if not serializer.is_valid():
            response = {
                'status': 'FAILURE',
                'data': serializer.errors
            }
            return Response(response, status=400)

        flower = serializer.create(serializer.validated_data)
        serializer = StoreSerializer(flower)
        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=201)

    def retrieve(self, request, pk=None):
        flower = Store.objects.filter(id=pk).last()
        serializer = StoreSerializer(flower)
        if not flower:
            response = {
                'status': 'FAILURE',
                'data': 'No matching flower'
            }
            return Response(response, status=400)

        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=200)

    def update(self, request, pk=None):
        serializer = StoreSerializer(data=self.request.data)
        flower = Store.objects.filter(id=pk).last()
        if not flower:
            response = {
                'status': 'FAILURE',
                'errors': 'No matching flower'
            }
            return Response(response, status=400)
        if not serializer.is_valid():
            response = {
                'status': 'FAILURE',
                'errors': serializer.errors
            }
            return Response(response, status=400)

        updated_data = serializer.update(flower, serializer.validated_data)
        serializer = StoreSerializer(updated_data)

        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=200)
