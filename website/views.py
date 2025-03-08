from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, RecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are Successfully Registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def customer(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.filter(id=pk).first()
        if record:
            return render(request, 'record.html', {'record': record})
        else:
            messages.error(request, 'Record does not exist')
            return redirect('home')
    else:
        messages.error(request, 'You must be logged in to view that page')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.filter(id=pk).first()
        record.delete()
        messages.success(request, 'Record deleted')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged to do that')
        return redirect('home')

def add_record(request):
    form = RecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added')
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to do that')
        return render(request, 'home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.filter(id=pk).first()
        form = RecordForm(request.POST or None, instance=record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated')
                return redirect('home')
        else:
            return render(request, 'update_record', {'form': form})
    else:
        messages.error(request, 'You must be logged in to do that')
        return redirect('home')
    