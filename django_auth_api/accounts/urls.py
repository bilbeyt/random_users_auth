from accounts.views import CustomUserAPIView
from django.urls import path


urlpatterns = [
    path("users/", CustomUserAPIView.as_view(), name="users")
]