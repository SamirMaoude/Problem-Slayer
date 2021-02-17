from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from .forms import ProblemSlayerUserForm

class IndexView(generic.TemplateView):

    template_name = 'home.html'


class SignUpView(generic.CreateView):

    form_class = ProblemSlayerUserForm

    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'


# Create your views here.



