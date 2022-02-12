from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from question.models import QuestionAnswered


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')

    if not email or not name or not password:
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except Exception:
        return render(request, 'accounts/register.html')

    User.objects.create_user(email=email, password=password, username=name)

    return redirect('login')


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    name = request.POST.get('name')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=name, password=password)

    if not user:
        return render(request, 'accounts/login.html')

    auth.login(request, user)
    return redirect('dashboard')


def logout(request):
    return render(request, 'accounts/logout.html')


@login_required(redirect_field_name='login')
def log_questions(request):
    user = request.user

    context = {
        'questions_ansered': QuestionAnswered.objects.filter(user=user).order_by('-created_at'),
    }

    return render(request, 'accounts/log_questions.html', context=context)
