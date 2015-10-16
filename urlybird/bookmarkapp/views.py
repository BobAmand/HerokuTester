from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def registration():
    pass


class UserCreateView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/register'

    def form_valid(self, form):
        form.save()
        # user = authenticate(username=self.request.user.username,
        #                     password=self.request.user.password)
        # login(self.request, user)
        return super(UserCreateView, self).form_valid(form)
