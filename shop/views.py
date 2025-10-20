from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import User

from shop.form import LoginForm, RegisterForm
from .models import Meuble
# from .form import *   # décommente si tu utilises des forms.py

def liste(request):
    meubles = Meuble.objects.all()
    return render(request, 'shop/liste.html', {'meuble': meubles})

def about(request):
    return render(request,'shop/about.html')

# Page détail du meuble (avant de commander)
@login_required(login_url='login')
def commander(request, meuble_id):
    meuble = get_object_or_404(Meuble, id=meuble_id)
    context = {'meuble': meuble}
    return render(request, 'shop/commande_detail.html', context)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après inscription
            messages.success(request, "Inscription réussie !")
            return redirect("liste")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = RegisterForm()

    return render(request, "shop/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form =LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} !")
            return redirect("liste")
        else:
            messages.error(request, "Nom d’utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()

    return render(request, "shop/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté.")
    return redirect("login")
