from django.urls import path, include
from rest_framework import routers
from store import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='cortinus_rest_framework'))
]
