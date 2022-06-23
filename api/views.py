from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Collection, Picture, CustomUser, Service, Review, Order, Chat, Message
from .permissions import IsAdminOrReadOnly
from .serializers import CollectionSerializer, PictureSerializer, UserSerializer, ServiceSerializer, ReviewSerializer, \
    OrderSerializer, ChatSerializer, MessageSerializer, MakeReviewSerializer

from .pusher import pusher_client


class PortfolioAPIList(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)


class PortfolioAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PortfolioPicturesAPIList(generics.ListCreateAPIView):
    serializer_class = PictureSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Picture.objects.filter(collection=pk)


class PictureAPIList(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PictureAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (IsAdminOrReadOnly,)


class UserAPIList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ServiceAPIList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ServiceAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ReviewAPIList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class ReviewAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAdminOrReadOnly,)


class MakeReviewAPIList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = MakeReviewSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class MakeReviewAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = MakeReviewSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class OrderAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OrderAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ChatAPIList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAdminUser,)


class ChatAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        pusher_client.trigger('chat', 'message', {
            'user': request.data['user'],
            'text': request.data['text'],
        })
        return super().post(request, *args, **kwargs)


class MessageAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
