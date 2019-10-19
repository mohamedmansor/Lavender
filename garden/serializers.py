from rest_framework import serializers


class FlowerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=200)
    picture = serializers.ImageField(max_length=200)
    info = serializers.CharField(max_length=500)

class FlowerSerializer(serializers.Serializer):
    tag = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
