from django import forms
from django.contrib.auth.models import User

class userForm(forms.ModelForm):

    # password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Senha')

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']
        labels = {
            'username' : 'Nome de Usuário',
            'password':'Senha',
            'first_name' : "Primeiro nome",
            'last_name' : "Sobrenome",
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2',)
        email = self.cleaned_data.get('email', None)
        user = self.cleaned_data.get('username', None)

        if password and password != password2:
            self.add_error('password2', "A senhas informadas são diferentes.")

        if User.objects.filter(email=email).exists():
            self.add_error('email',"Este e-mail já está sendo utilizado.")

        if email == None or email == '':
            self.add_error('email',"é necessário preencher o campo email.")
        
        if user == None or len(user) < 5 :
            self.add_error('username',"O nome de usuário precisa ter no minimo 5 caracteres.")
        
        if User.objects.filter(username=user).exists():
            self.add_error('username',"Este nome de usuário já está sendo usado, escolha outro.")

        return self.cleaned_data