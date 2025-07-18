from django.shortcuts import render, redirect
from .models import Todo


def todolist(request):
    todos = Todo.objects.all() 
    return render(request, 'todolist.html', {'todos': todos})


def createtodo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Todo.objects.create(title=title, description=description)

    return redirect('todolist')  

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todolist')  
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect('todolist')  

