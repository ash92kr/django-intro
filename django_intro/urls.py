"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django_app import views   # url 파일은 views를 이동시킴
from app_intro import views   # 설정한 앱이름의 폴더 안에 있는 views 파일 참고

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),   # url이 오면 메소드를 실행해야 한다
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    path('hello/<str:name>/', views.hello),   # 이름이 들어오면 hello를 출력함
    path('cube/<int:num>', views.cube),
    path('todos/', include('todo.urls'))
    
]
