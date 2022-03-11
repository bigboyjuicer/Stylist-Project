from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from .models import Portfolio


# Create your views here.
def index(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list
    }
    return render(request, 'portfolio/index.html', context)


def detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio})
