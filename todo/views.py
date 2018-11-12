from django.shortcuts import render, redirect
from todo.models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos' : todos})


def new(request):
    return render(request, 'todo/new.html')  # 사용자가 입력할 수 있는 폼 만들기

# read / create - new.html을 통한 create.html로 출력(get 방식)    
def create(request):
    title = request.POST.get('title')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title, deadline=deadline)    
    todo.save()   # db.session.add() + db.session.commit()과 동일    
    
    return redirect('/todos/')

def read(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/read.html', {'todo': todo})
    
# read/create 합치기 - todo_create.html을 통한 get 방식 입력 후 todo_create.html로 출력
def todo_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        # Todo(title = title, deadline = deadline)
        # todo.save()
        Todo.objects.create(title=title, deadline=deadline)  # 위 2문장을 합친 것(save가 자동으로 됨)
        return redirect('/todos/')
    else:
        return render(request, 'todo/todo_create.html')
    

def update(request, id):
    todo = Todo.objects.get(id=id)  # 기존 id에 해당하는 objects(todo)를 가져옴
    if request.method == "POST":
        # 저장로직
        todo.title = request.POST.get('title')
        todo.deadline = request.POST.get('deadline')
        todo.save()
        
        return redirect('/todos/')
        
    else:
        # 폼 보여주기(버튼을 누르면 get 방식)
        deadline = todo.deadline.strftime("%Y-%m-%d")  # datetime은 datetime 객체이므로 형식이 지정되어 있음
      # deadline = "{}-{}-{}".format(todo.deadline.your, todo.deadline.month, todo.deadline.day)   # 둘 다 가능
        return render(request, 'todo/update.html', {'todo': todo, 'deadline': deadline})
        
        
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos/')


