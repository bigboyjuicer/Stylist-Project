from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.http import Http404
from rest_framework import viewsets, permissions

from .serializers import PortfolioSerializer
from .models import Portfolio, Picture

# Create your views here.


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class IndexView(generic.ListView):
    model = Picture
    template_name = 'portfolio/index.html'
    context_object_name = 'picture_list'


class DetailView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/detail.html'


def index(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list
    }
    return render(request, 'portfolio/index.html', context)


def detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio})
