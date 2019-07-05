from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('admin/', views.admin, name='admin'),
]
