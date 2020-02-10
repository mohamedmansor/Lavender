from rest_framework import serializers
from store.models import Store
from garden.serializers import FlowerSerializer, CategorySerializer


class StoreSerializer(serializers.Serializer):
    store_name = serializers.CharField(max_length=200, required=True)
    is_online = serializers.BooleanField(required=True)
    # location = 
    def create(self, validated_data):
        """
        Create and returns a new `Store` instance, given the validated data.
        """
        store = Store.objects.create(
            name=validated_data.get('store_name'),
            is_online=validated_data('is_online'),
        )
        return store

    def update(self, instance, validated_data):
        """
        Update and return an existing `Store` instance, given the validated data.
        """
        instance.name = validated_data.get('store_name', instance.name)
        instance.name = validated_data.get('is_online', instance.name)
        instance.save()
        return instance
