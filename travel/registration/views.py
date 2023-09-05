from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# from .models import Place, team


# Create your views here.
# def demo(request):
    # place = Place.objects.all()
    # team_obj = team.objects.all()
    # return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):

    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, " username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, " email exists")

                return redirect('register')
            else:

                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                                password=password)
                user.save()
                print("created")
                return redirect('login')
        else:
            messages.info(request, " pass not matching")
            return redirect('register')

    return render(request, "register.html")

