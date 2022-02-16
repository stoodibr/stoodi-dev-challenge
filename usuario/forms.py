from django import forms
from .models import Usuario

class UsuarioRegisterForm(forms.ModelForm):
    
    nome = forms.CharField(label='Nome' , help_text='Campo obrigatório como todos os que tiverem *' )
    email = forms.EmailField(label= 'Email *', max_length=100)
    
    password = forms.CharField(label= "Senha", widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['nome','email','password']