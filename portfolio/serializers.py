from .models import Portfolio
from rest_framework import serializers


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'cover_picture']
