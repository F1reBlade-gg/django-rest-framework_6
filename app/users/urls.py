from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.users.views import RegisterAPIVIew, ProfileAPIVIew

urlpatterns = [
    path("register", RegisterAPIVIew.as_view(), name='register'),
    path("login", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path("profile", ProfileAPIVIew.as_view(), name='profile'),
]
