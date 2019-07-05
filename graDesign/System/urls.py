from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('query/', views.query, name='query'),
    path('return/', views.Return, name='return'),
    path('info/', views.info, name='info'),
    path('borrowbook/', views.borrowbook, name='borrowbook'),
    path('ReturnBook/', views.ReturnBook, name='ReturnBook'),
    path('logout/', views.logout, name='logout'),
]
