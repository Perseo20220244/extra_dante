from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        login_form = CustomLoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            password = request.POST['password']
            login(request, user)
            request.session['password_plain'] = password  # Guardar la contraseña en sesión
            return redirect('home')
    else:
        login_form = CustomLoginForm()

    return render(request, 'users/login_form.html', {'login_form': login_form})

def register_view(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(register_form.cleaned_data['password1'])
            user.save()
            return redirect('login')  # Redirigir al login después de registrar
    else:
        register_form = UserRegistrationForm()

    return render(request, 'users/register_form.html', {'register_form': register_form})

@login_required
def home_view(request):
    password_plain = request.session.get('password_plain', 'No password found')
    return render(request, 'users/home.html', {'password_plain': password_plain})

def logout_view(request):
    logout(request)
    return redirect('login')
