from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.index, name = 'index'),
    path('', views.homepage, name = 'homepage'),
    path('recursive/', views.recursive, name = 'recursive'),
    path('iterative/', views.iterative, name = 'iterative'),
    
]