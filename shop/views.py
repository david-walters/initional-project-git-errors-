from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Perfume

def index(request):
    if not request.user.is_authenticated:
        return redirect('register')
    perfumes = Perfume.objects.all()
    return render(request, 'index.html', {'perfumes': perfumes})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def perfume_detail(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    return render(request, 'perfume_detail.html', {'perfume': perfume})

@login_required
def cart(request):
    return render(request, 'cart.html')
