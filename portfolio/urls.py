from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.PortfolioViewSet)

app_name = 'portfolio'
# urlpatterns = [
#    path('', include(router.urls)),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    #path('', views.IndexView.as_view(), name='index'),
#    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
# ]

urlpatterns = router.urls
