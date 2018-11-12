from django.urls import path
from . import views   # 현재 폴더의 views.py 추가

app_name = 'todo'

urlpatterns = [
    # 이 아래 들어가는 url들의 앞에 todos/가 생략되었음
    path('', views.index),
    path('new/', views.new),   # todo/new가 오면 todo new를 실행함
    path('create/', views.create), 
    path('<int:id>/', views.read),
    path('todo_create/', views.todo_create),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
    
]