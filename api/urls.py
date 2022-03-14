from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.PortfolioAPIView.as_view()),
    path('portfolio/<int:pk>/', views.PortfolioDetailAPIView.as_view())
]