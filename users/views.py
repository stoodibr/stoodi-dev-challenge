from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login


class AuthenticationView(LoginView):
    template_name = "users/authentication.html"


class RegistrationView(FormView):
    success_url = '/'
    template_name = 'users/registration.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        self.object = form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
        login(self.request, new_user)
        return super().form_valid(form)