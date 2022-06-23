from rest_framework import serializers

from .models import Collection, Picture, CustomUser, Service, Review, Order, Chat, Message


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'image', 'collection', 'created')


class CollectionSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'title', 'pictures', 'cover_picture', 'created')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'price')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'service', 'user_phonenumber', 'comment', 'is_accepted', 'is_completed', 'created',
                  'time_accepted', 'time_completed')


class UserOrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id', 'user', 'service', 'comment', 'is_accepted', 'is_completed', 'created', 'time_accepted',
            'time_completed')


class UserSerializer(serializers.ModelSerializer):
    orders = UserOrderSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'orders', 'chat', 'first_name', 'last_login', 'date_joined', 'is_staff', 'is_active')


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ('id', 'content', 'user', 'created')


class MakeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'user', 'created')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'date', 'user', 'chat')


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = ('id', 'user', 'messages')
