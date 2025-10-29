from django.shortcuts import render, redirect
from .firebase_config import get_todo_ref

def todolist(request):
    todo_ref = get_todo_ref()
    todos = todo_ref.get()
    todos_list = []

    if todos:
        for key, value in todos.items():
            todos_list.append({
                'id': key,
                'title': value.get('title', ''),
                'description': value.get('description', ''),
                'completed': value.get('completed', False),
            })

    return render(request, 'todolist.html', {'todos': todos_list})


def createtodo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        todo_ref = get_todo_ref()
        todo_ref.push().set({
            'title': title,
            'description': description,
            'completed': False
        })

    return redirect('todolist')


def complete_todo(request, todo_id):
    todo_ref = get_todo_ref()
    todo_ref.child(todo_id).update({'completed': True})
    return redirect('todolist')


def delete_todo(request, todo_id):
    todo_ref = get_todo_ref()
    todo_ref.child(todo_id).delete()
    return redirect('todolist')
