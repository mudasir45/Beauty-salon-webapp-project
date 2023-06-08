from django.urls import path
from . import views

urlpatterns = [
    path('userLogin/', views.user_login, name='user_login' ),
    path('userSignUp/', views.user_SignUp, name='user_SignUp' ),
]
