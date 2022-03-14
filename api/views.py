from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Collection, Picture
from .serializers import CollectionSerializer, PictureSerializer


class PortfolioAPIView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class PortfolioDetailAPIView(APIView):
    def get(self, request, pk):
        portfolio = Collection.objects.get(pk=pk)
        collection = Picture.objects.filter(collection=pk)
        return Response({'portfolio': CollectionSerializer(portfolio).data, 'collection': PictureSerializer(collection, many=True).data})
