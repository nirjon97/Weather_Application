from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login


# Create your views here.

def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('city_weather')

        else:
            messages.warning(request, 'Your username or password is invalid.')
    

    context = {

    }
    return render(request,"log_in.html",context)

def logoutView(request):
    logout(request)
    return redirect('loginView')

def registerView(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('loginView')


    context = {
       'form': form
    }
    return render(request,"register.html",context)