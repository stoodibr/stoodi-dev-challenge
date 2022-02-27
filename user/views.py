from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import userForm
from django.contrib.auth.decorators import login_required


def signin(request):
    erros = {}
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == '' or senha == '':
            erros['campo_vazio'] = 'email ou senha inválidos'
        else:
            if User.objects.filter(email=email).exists():
                pessoa = User.objects.get(email=email)
                user = auth.authenticate(request, username=pessoa.username, password=senha)
                if user is not None:
                    auth.login(request, user)
                    return redirect('question')    
                else:
                    erros['senha_invalida'] = 'senha inválida'
                    erros['email'] = email
            else:
                erros['senha_invalida'] = 'Email Incorreto'
                        
    return render (request, 'signin.html', erros)

def signup(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            user = User.objects.create_user(
                                        username=new_user.username,
                                        email=new_user.email,
                                        first_name=new_user.first_name,
                                        last_name=new_user.last_name,
                                        password=new_user.password
                                    )
            user.save()
            auth.login(request, user)
            return redirect('question')
        else:
            context = {'form_new_user' : form }
            return render(request, 'signup.html', context)        
    
    form = userForm()
    context = {'form_new_user' : form }
    return render(request, 'signup.html', context)      

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('question')