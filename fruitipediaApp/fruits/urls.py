"""
URL configuration for fruitipediaApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index_view, dashboard_view, create_fruit_view,\
    fruit_details_view, edit_fruit_view,delete_fruit_view, create_category_view


urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create-fruit/', create_fruit_view, name='create_fruit'),
    path('<int:pk>/', include([
    path('fruit-detail/', fruit_details_view, name='fruit_detail'),
        path('edit-fruit/', edit_fruit_view, name='edit_fruit'),
        path('delete-fruit/', delete_fruit_view, name='delete_fruit'),

    ])),
    path('create-category/', create_category_view, name='create_category'),

]
