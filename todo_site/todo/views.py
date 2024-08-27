from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


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

class Registration(CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url='acc/login'