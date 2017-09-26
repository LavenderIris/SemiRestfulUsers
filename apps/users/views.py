from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User

def index(request):
    return render(request,'index.html', {"users": User.objects.all() })

def show_add_user(request):
    return render(request, 'add_user.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/new')
        else:
            myUser = User.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'])
            myUser.save()
        
    return redirect('/users/new')

def show(request, id):
    if request.method == 'GET':
        return render(request,'show_user.html', {'user': User.objects.get(id=id)})

def edit_page(request, id):
     if request.method == 'GET':
        return render(request,'edit_user.html', {'user': User.objects.get(id=id)})
           

def update(request):
    if request.method == 'POST':
        myresult=request.POST
        print "results", myresult
        myUser = User.objects.get(id=myresult['id'])
        myUser.first_name = myresult['first_name']
        myUser.last_name = myresult['last_name']
        myUser.email = myresult['email']
        myUser.save()
    
    return redirect('/users/new')

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')