from django.contrib import admin
from todo.models import Todo   # todo라는 모델의 Todo 클래스 가져오기

# Register your models here.
admin.site.register(Todo)
