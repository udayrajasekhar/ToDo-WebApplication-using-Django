from django.contrib import admin
from django.urls import path,include
from tasks import views



urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:pk>', views.deleteTask, name='delete')
]