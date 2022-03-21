from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse

from user.constants import (
    QS_REDIRECT_SIGNUP_ERROR,
    QS_REDIRECT_LOGIN_ERROR,
    QS_REDIRECT_LOGOUT,
    SIGNUP_TEMPLATE,
    LOGIN_TEMPLATE
)
from user.exceptions.signup import SignupDataInvalid
from user.utils.signup_validator import signup_validator
from user.models import CustomUser


def signup(request):
    return render(request, SIGNUP_TEMPLATE, context={})


def signup_validation(request):
    try:
        user_data_validated = signup_validator(
            request.POST.get('user_email'),
            request.POST.get('user_password'),
            request.POST.get('user_name')
        )

        user_data_validated['is_staff'] = False
        user_data_validated['is_superuser'] = False

        user = CustomUser.objects.create_user(**user_data_validated)
        user = authenticate(
            username=request.POST.get('user_email'),
            password=request.POST.get('user_password')
        )

        login(request, user)

    except SignupDataInvalid as serr:
        return redirect(
            reverse('signup') + QS_REDIRECT_SIGNUP_ERROR[serr.code])

    except Exception:
        return redirect(
            reverse('signup')
            + QS_REDIRECT_SIGNUP_ERROR['GENERAL_ERROR']
        )
    else:
        return redirect(reverse('question'))


def vwlogin(request):
    return render(request, LOGIN_TEMPLATE)


def login_validation(request):
    user_email = request.POST.get('user_email')
    user_password = request.POST.get('user_password')

    user = authenticate(username=user_email, password=user_password)

    if user is not None:
        login(request, user)
        return redirect(reverse('question'))
    else:
        return redirect(
            reverse('login') + QS_REDIRECT_LOGIN_ERROR['INVALID_LOGIN'])


def vwlogout(request):
    logout(request)
    return redirect(
        reverse('login') + QS_REDIRECT_LOGOUT['SUCCESS_LOGOUT'])
