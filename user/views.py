from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def sign_in(request):
    if(request.method == 'GET'):
        return render(request, 'auth/sign_in.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_auth = authenticate(username=username, password=password)
        if(user_auth):
            login(request, user_auth)
            context = {
                'message_text': 'Usuário logado com sucesso! :D',
                'success': True
            }
            return render(request, 'auth/sign_in.html', context=context)
        else:
            context = {
                'message_text': 'Username ou senha inválidos! D:',
                'success': False
            }
            return render(request, 'auth/sign_in.html', context=context, status=401)


def sign_up(request):
    if(request.method == 'GET'):
        return render(request, 'auth/sign_up.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if(user):
            context = {
                'message_text': 'Usuário já cadastrado! :O',
                'success': False
            }
            return render(request, 'auth/sign_up.html', context=context, status=409)

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()

        context = {
            'message_text': 'Cadastrado realizado com sucesso! :D',
            'success': True
        }
        return render(request, 'auth/sign_up.html', context=context)
