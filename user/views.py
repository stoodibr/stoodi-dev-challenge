from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from question.models import LogAnswers, Question


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


@login_required(login_url='/login')
def user_log(request):
    data = LogAnswers.objects.filter(
        user=request.user).order_by('creation_date')

    for item in data.values():
        item['question'] = Question.objects.get(id=item['question_id'])

    headers = [
        'Questão',
        'Resposta',
        'Resultado',
        'Resposta correta',
        'Data da tentativa',
    ]
    context = {
        'headers': headers,
        'data': data
    }

    return render(request, 'log.html', context=context)
