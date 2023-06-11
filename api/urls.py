"""
URL configuration for drf_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('post/', views.PostListAPIView.as_view(), name="product_list"),
    path('post/create/', views.PostCreateAPIView.as_view(), name="product_create"),
    path('post/<int:pk>/update/', views.PostUpdateAPIView.as_view(), name="product_update"),
    path('post/<int:pk>/delete/', views.PostDestroyAPIView.as_view(), name="product_delete"),
    path('post/<int:pk>/', views.PostDetailAPIView.as_view(), name="product_detail"),
]
