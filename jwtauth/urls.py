from django.urls import path

from jwtauth.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register')
]
