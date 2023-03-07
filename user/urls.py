from django.urls import path 
from .views import *
urlpatterns = [
    path("",Index,name="index"),
    path("register/",Register,name="register"),
    path("login/",Login,name="login"),
    path("logout/",Logout,name="Logout"),
    path("<str:pk>/",Change,name="change"),




]
