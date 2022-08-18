from django import forms

class CadastroForm(forms.Form):   
    username = forms.CharField(label = 'Usuário')
    password1 = forms.CharField(label = 'Senha', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirma Senha', widget = forms.PasswordInput)