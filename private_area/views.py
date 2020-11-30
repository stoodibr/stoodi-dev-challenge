from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from question.models import Response

class SubscriptionView(TemplateView):
    def get(self, request):
        return render(request, 'private_area/subscription.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password, is_staff=False)

        return render(request, 'private_area/subscription_confirmation.html', context={'username': user.username})


class LoginView(TemplateView):
    def get(self, request):
        return render(request, 'private_area/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.get(username=username)

        if user.check_password(password):
            request.session['user_id'] = user.id

        return redirect(reverse('question'))


class LogQuestionView(TemplateView):
    def get(self, request):
        if not request.session['user_id']:
            return redirect(reverse('login'))

        responses = [response.to_dict() for response in Response.objects.filter(user_id=request.session['user_id'])]

        context = {
            'responses': responses
        }

        return render(request, 'private_area/log_questions.html', context=context)
