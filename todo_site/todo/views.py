from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    list_items=Todo.objects.order_by("-date")
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo'))
    form = TodoForm()
    page={
        "form":form,
        "list":list_items,
        "title":"TODOLIST"
    }
    return render(request,'todo/index.html',page)

def remove(request,itemID):
    item=Todo.objects.get(id=itemID)
    item.delete()
    messages.info(request,"item removed")
    return HttpResponseRedirect(reverse('todo'))
