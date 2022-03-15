from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Collection, Picture
from .permissions import IsAdminOrReadOnly
from .serializers import CollectionSerializer, PictureSerializer


class PortfolioAPIView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PortfolioDetailAPIView(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, pk):
        collection = Collection.objects.get(pk=pk)
        pictures = Picture.objects.filter(collection=pk)
        return Response({'collection': CollectionSerializer(collection).data,
                         'pictures': PictureSerializer(pictures, many=True).data})

    def post(self, request, pk):
        request.data['collection'] = pk
        serializer = PictureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'picture': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = request.data['pk']
        print(pk)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        picture = Picture.objects.get(pk=pk)
        picture.delete()

        return Response({"picture": "Deleted picture " + str(pk)})