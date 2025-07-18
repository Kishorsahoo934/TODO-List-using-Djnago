from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todolist, name='todolist'),  # ✅ Show To-Do List on Home Page
    path('createtodo/', views.createtodo, name='createtodo'),  # ✅ Separate Add URL
    path('complete_todo/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    
]
