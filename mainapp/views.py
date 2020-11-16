from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mainapp.forms import RegisterForm

# Create your views here.

def index(request):
    values = {
        'title':'Index'
    }
    return render(request, 'index.html', values)

def register_user(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Registro completo')
                return redirect('index')

        values = {
            'title':'registro',
            'register_form':register_form
        }
        return render(request, 'users/register.html', values)

def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user.name}')
                return redirect('index')

            else:
                messages.warning(request, 'Usuario incorrecto')

        values = {
            'title':'Login'
        }

        return render(request, 'users/login.html', values)

def logout_user(request):
    logout(request)
    return redirect(login)