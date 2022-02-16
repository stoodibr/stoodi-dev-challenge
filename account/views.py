from django.forms import ModelForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


def login_form_view(request, template_name='account/pages/login.html'):
    return render(request, template_name)


def register_form_view(request, template_name='account/pages/cadastro.html'):
    return render(request, template_name)


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, "Você precisa preencher todos os campos")
            return redirect('register_form_view')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Esse e-mail já está cadastrado!")
            return redirect('register_form_view')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse nome de usuário já está cadastrado!")
            return redirect('register_form_view')

        User.objects.create_user(username, email, password)
        messages.success(request, "Conta criada com sucesso, faça login.")
        return redirect('question')


def auth_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso")
            return redirect('question')
        else:
            messages.error(request, "Não foi possível logar. Tente novamente!")
            return redirect('login_form_view')


def logout_user(request):
    logout(request)
    messages.warning(request, "Você deslogou!")
    return redirect('question')
