from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('drf-auth/', include('rest_framework.urls')),
    path('portfolio/', views.PortfolioAPIList.as_view()),
    path('portfolio/<int:pk>/', views.PortfolioAPIDetailView.as_view()),
    path('portfolio/<int:pk>/pictures/', views.PortfolioPicturesAPIList.as_view()),
    path('pictures/', views.PictureAPIList.as_view()),
    path('pictures/<int:pk>/', views.PictureAPIDetailView.as_view()),
    path('users/', views.UserAPIList.as_view()),
    path('users/<int:pk>', views.UserAPIDetailView.as_view()),
    path('service/', views.ServiceAPIList.as_view()),
    path('service/<int:pk>/', views.ServiceAPIDetailView.as_view(), name='service-detail'),
    path('review/', views.ReviewAPIList.as_view()),
    path('review/<int:pk>/', views.ReviewAPIDetailView.as_view()),
    path('order/', views.OrderAPIList.as_view()),
    path('order/<int:pk>/', views.OrderAPIDetailView.as_view()),
]
