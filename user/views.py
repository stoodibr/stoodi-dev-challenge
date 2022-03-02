from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm
from django.contrib.auth.decorators import login_required


def signin(request):
    erros = {}
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == '' or senha == '':
            erros['empty_field'] = 'email ou senha inválidos'
        else:
            if User.objects.filter(email=email).exists():
                pessoa = User.objects.get(email=email)
                user = auth.authenticate(request, username=pessoa.username, password=senha)
                if user is not None:
                    auth.login(request, user)
                    return redirect('question')    
                else:
                    erros['incorrect_input'] = 'Senha Inválida'
                    erros['email'] = email
            else:
                erros['incorrect_input'] = 'Email Incorreto'
                        
    return render (request, 'signin.html', erros)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
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
       
        context = {'form_new_user' : form }
        return render(request, 'signup.html', context)        
    
    form = UserForm()
    context = {'form_new_user' : form }
    return render(request, 'signup.html', context)      

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('question')