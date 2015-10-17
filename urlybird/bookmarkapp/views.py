from django.contrib.auth import authenticate, login  # , logout
# from django.shortcuts import render
# from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from bookmarkapp.models import Bookmark

from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView


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


class UserDetailView(DetailView):
    """Used to view a User and their list of bookmarks"""
    model = User
    template_name = 'bookmarkapp/user_detail.html'
    paginate_by = 10

    # queryset = Bookmark.objects.get(author=self.user)

    # def get_context_data(self, **kwargs):
    #     context = super(UserDetailView, self).get_context_data(**kwargs)
    #     return context
