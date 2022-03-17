from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from question.models import Answers


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request,'user/login.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'form':form})


def create_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(request, username=username, password=raw_password)
        login(request, user)
        return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})
    

def logout_user(request):
    logout(request)
    return redirect('index')


def log_questions(request):
    if request.user.is_authenticated:
        answers = Answers.objects.filter(user= request.user)
        return render(request, 'user/log_questions.html', {'answers': answers})
    else:
        return redirect('index')