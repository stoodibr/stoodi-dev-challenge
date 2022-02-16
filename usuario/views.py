from django.views.generic import TemplateView
from usuario.forms import UsuarioRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse

from usuario.models import Usuario

class UsuarioRegisterView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'usuario_register_form.html'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UsuarioRegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse('usuario_register_success')
        
# Create your views here.
class UsuarioRegisterSuccessView(TemplateView):
    template_name= 'usuario_register_success.html'