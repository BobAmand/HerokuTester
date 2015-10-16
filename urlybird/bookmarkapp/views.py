from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            profile = Profile(
                user=user,
                favorite_color='blue',
            )
            profile.save()

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('recent_statuses')
    else:
        form = UserForm()
    return render(request, 'registration/register.html',
                  {'form': form})


class UserCreateView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/register'

    def form_valid(self, form):
        new_user = form.save()
        user = authenticate(username=new_user.username,
                            password=form.cleaned_data['password1'])
        login(self.request, user)
        return super(UserCreateView, self).form_valid(form)
