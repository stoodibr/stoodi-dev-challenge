#coding: utf8
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .models import BD
from django.contrib.auth.models import User

def question(request):
    text = 'Quanto é 2^5?'

    # BUG: as respostas estão ficando fora de ordem
    answers = {
        'a': '0',
        'b': '2',
        'c': '16',
        'd': '32',
        'e': '128',
    }

    context = {
        'question_text': text,
        'answers': answers,
    }

    return render(request, 'question/question.html', context=context)


def cad(request):
    return render(request, 'cadastro/cadastro.html')


def log(request):
    return render(request, 'login/login.html')


def question_answer(request):
    form = BD.setAnswer(request.POST.get('answer', 'z'))
    resp = BD.getAnswer()
    is_correct = resp == 'd'

    context = {
        'is_correct': is_correct,
    }

    return render(request, 'question/answer.html', context=context)


def authLogin(request):
    print(request.POST.get['nome_login'])
    print(request.POST.get['pass_login'])
    username = request.POST['nome_login']
    password = request.POST['pass_login']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render('/questao')
        ...
    else:
        return render('/')

def create_user(request):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.save()
    return render(request, 'login/login.html')
# def Register(request):
#     form = Log.setNewRegister(request.POST.get('nome', 'z'), request.POST.get('email', 'z'), request.POST.get('password', 'z') )
#     return render(request, 'login/login.html')

