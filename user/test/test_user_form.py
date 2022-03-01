from user.forms import UserForm
from .base_model import BaseModel


class UserFormTestCase(BaseModel):

    def test_userform_labels(self):

        self.assertEqual(self.user_form.fields['username'].label, 'Nome de Usuário')
        self.assertEqual(self.user_form.fields['email'].label, 'Email')
        self.assertEqual(self.user_form.fields['password'].label, 'Senha')
        self.assertEqual(self.user_form.fields['password2'].label, 'Confirmar Senha')
        self.assertEqual(self.user_form.fields['first_name'].label, 'Primeiro nome')
        self.assertEqual(self.user_form.fields['last_name'].label, 'Sobrenome')

    def test_number_of_fields(self):
        self.assertEqual(len(self.user_form.fields), len(['username','email','first_name','last_name','password', 'password2']))
    
    def test_clean_password_field(self):
        form = UserForm(data={"password": "123", "password2" : "233"})
        self.assertEqual(form.errors["password2"], ["A senhas informadas são diferentes."])

    def test_clean_email_field(self):
        form = UserForm(data={"email": ""})
        self.assertEqual(form.errors["email"], ["é necessário preencher o campo email."])
    
    def test_clean_username_field(self):
        form = UserForm(data={"username": "123"})
        self.assertEqual(form.errors["username"], ["O nome de usuário precisa ter no mínimo 5 caracteres."])
    
    def test_clean_username_field_in_use(self):
        form = UserForm(data={"username": self.user.username})
        self.assertEqual(form.errors["username"], ["Este nome de usuário já está sendo usado, escolha outro."])