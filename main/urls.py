from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('services/', views.shop, name='shop' ),
    path('CategoryFilter/<int:id>', views.CategoryFilter, name='CategoryFilter' ),
    path('ServiceDetails/<int:id>', views.ServiceDetails, name='ServiceDetails' ),
    path('CheckOut/<int:id>', views.CheckOut, name='CheckOut' ),
]
