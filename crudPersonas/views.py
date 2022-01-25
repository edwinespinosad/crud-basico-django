from django.shortcuts import render, redirect
from django.template import context
from .models import User
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    users = User.objects.all()

    paginator = Paginator(users, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'create/home.html', context={'users':page_obj})

def create(request):
    return render(request, 'create/create.html')

def registerUser(request):
    name = request.POST['name']
    last_name = request.POST['lastname']
    user = User.objects.create(name=name, last_name=last_name)

    messages.success(request,"User created successfully!")
    return redirect('/')

def delete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    messages.success(request,"User deleted successfully!")
    return redirect('/')

def edit(request, id):
    user = User.objects.get(id = id)
    return render(request, 'create/edit.html', {'user': user})

def saveEdit(request):
    id = request.POST['id']
    name = request.POST['name']
    last_name = request.POST['lastname']

    user = User.objects.get(id = id)

    user.name = name
    user.last_name = last_name
    user.save()
    messages.success(request,"User edited successfully!")

    return redirect('/')