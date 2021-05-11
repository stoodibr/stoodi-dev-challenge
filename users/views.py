from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Created user {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_log(request):
    user = request.user.username
    try:
        with open(f'logs/{user}-questions.log') as file:
            logs = file.read().replace('{', ' ').split('}')
    except FileNotFoundError:
        logs = None
    context = {'logs': logs}
    return render(request, 'users/question_logs.html', context=context)
