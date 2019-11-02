from rest_framework import serializers
from .models import Flower, Category


class FlowerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=True)
    category = serializers.CharField(max_length=200, required=True)
    # picture = serializers.ImageField(max_length=200, required=False)
    info = serializers.CharField(max_length=500, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Flower` instance, given the validated data.
        """
        category = Category.objects.filter(tag=validated_data.get('category')).last()
        if not category:
            category = Category.objects.create(tag=validated_data.get('category'))
        
        flower = Flower.objects.create(
            name=validated_data.get('name'),
            category=category,
            info=validated_data.get('name')
        )
        return flower

    def update(self, instance, validated_data):
        """
        Update and return an existing `Flower` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        # instance.category = validated_data.get('category', instance.category)
        # instance.picture = validated_data.get('picture', instance.picture)
        instance.info = validated_data.get('info', instance.info)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    tag = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        """
        Create and return a new `Category` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Category` instance, given the validated data.
        """
        instance.tag = validated_data.get('tag', instance.tag)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance
