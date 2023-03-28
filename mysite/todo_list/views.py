from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList

# Create your views here.
def index(request):
    return HttpResponse("Hello World!!!")

def read_list(request, list_id):
    todo_list = TodoList.objects.filter(id=list_id)