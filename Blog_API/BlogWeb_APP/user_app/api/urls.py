from django.contrib import admin
from django.urls import path
from user_app.api.views import register_view,logout_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',register_view,name="register"),
    path('login/',obtain_auth_token,name="login"),
    path("logout/",logout_view,name="logout"),
]
