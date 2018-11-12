from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),   # todo/new가 오면 todo new를 실행함
]


