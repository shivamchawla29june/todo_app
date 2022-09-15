from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def TodoApp(request) :
    todo_items = Todo.objects.all().order_by("added_date")
    return render(request, 'main/todo.html',{
        "todo_items": todo_items,
    })

@csrf_exempt
def add_todo(request):
    content = request.POST["content"]
    added_datetime = timezone.now()
    Todo.objects.create(added_date=added_datetime, text = content)
    #print(added_date,"   ", content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect("/")