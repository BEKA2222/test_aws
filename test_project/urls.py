from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserProfile, basename='users')
router.register(r'rating', RatingViewSet, basename='rating')
router.register(r'review', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

