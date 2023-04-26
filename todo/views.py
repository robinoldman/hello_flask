from django.shortcuts import render
from .models import Items
# Create your views here.


def get_todo_list(request):
    items = Items.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):

    return render(request, 'todo/add_item.html')
