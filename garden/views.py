import json

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Flower
from .serializers import CategorySerializer, FlowerSerializer


class FlowersViewSet(viewsets.ViewSet):
    serializer_class = FlowerSerializer

    def list(self, request):
        queryset = Flower.objects.all()
        serializer = FlowerSerializer(queryset, many=True)
        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=200)

    def create(self, request):
        serializer = FlowerSerializer(data=self.request.data)
        if not serializer.is_valid():
            response = {
                'status': 'FAILURE',
                'data': serializer.errors
            }
            return Response(response, status=400)

        flower = serializer.create(serializer.validated_data)
        serializer = FlowerSerializer(flower)
        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=201)

    def retrieve(self, request, pk=None):
        flower = Flower.objects.filter(id=pk).last()
        serializer = FlowerSerializer(flower)
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
        serializer = FlowerSerializer(data=self.request.data)
        flower = Flower.objects.filter(id=pk).last()
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
        serializer = FlowerSerializer(updated_data)

        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=200)


class CategoriesViewSet(viewsets.ViewSet):
    serializer_class = CategorySerializer

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        response = {
            'status': 'SUCCESS',
            'data': serializer.data
        }
        return Response(response, status=200)

    def create(self, request):
        serializer = CategorySerializer(data=self.request.data)
        if not serializer.is_valid():
            response = {
                'status': 'FAILURE',
                'data': serializer.errors
            }
            return Response(response, status=400)
        flower = serializer.create(serializer.validated_data)
        response = {
            'status': 'SUCCESS',
            'data': flower
        }
        return Response(response, status=201)

    def retrieve(self, request, pk=None):
        flower = Category.objects.filter(id=pk).last()
        if not flower:
            response = {
                'status': 'FAILURE',
                'data': 'No matching flower'
            }
            return Response(response, status=400)

        response = {
            'status': 'SUCCESS',
            'data': CategorySerializer(flower)
        }
        return Response(response, status=200)

    def update(self, request, pk=None):
        serializer = CategorySerializer(data=self.request.data)
        flower = Category.objects.filter(id=pk).last()
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
        response = {
            'status': 'SUCCESS',
            'data': CategorySerializer(updated_data)
        }
        return Response(response, status=200)
