from rest_framework import serializers
from .models import Collection, Picture


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'title', 'cover_picture', 'created')


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['id', 'image', 'collection', 'created']
