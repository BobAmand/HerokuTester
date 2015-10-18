from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class UserCreateView(FormView):
    """Used to register and log-in new users"""
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/register'

    def form_valid(self, form):
        new_user = form.save()
        user = authenticate(username=new_user.username,
                            password=form.cleaned_data['password1'])
        login(self.request, user)
        return super(UserCreateView, self).form_valid(form)
