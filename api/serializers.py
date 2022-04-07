from rest_framework import serializers

from .models import Collection, Picture, CustomUser, Service, Review, Order


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'image', 'collection', 'created')


class CollectionSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'title', 'pictures', 'cover_picture', 'created')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_login', 'date_joined', 'is_staff', 'is_active')
        read_only_fields = ()


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'price')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'user', 'created')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'service', 'is_accepted', 'is_completed', 'created', 'time_accepted', 'time_completed')
