from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from bookmarkapp.forms import BookmarkForm
from bookmarkapp.models import Bookmark


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


# class BookmarkAdd(FormView):
#     """Used to create bookmarks"""
#     """Want to add a bookmark to the list assoicated with the user"""
#     """ - Bob: look at 'UserCreationForm' in Django tutorials"""
#
#     template_name = 'addbookmark.html'
#     form_class = UserCreationForm
#     success_url = '/add'
#
#     def form_add(self, form):
#         new_bmk = form.save()

def addbookmark(request):
    form_class = BookmarkForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            title = request.POST.get('bkf_title', '')
            description = request.POST.get('bkf_description', '')
            original_url = request.POST.get('bkf_original_url', '')

            bookmark = Bookmark({
                'title': title,
                'description': description,
                'original_url': original_url,
            })
            bookmark.save()

            return redirect('addbookmark')

    return render(request, 'bookmarkapp/addbookmark.html', {
        'form': form_class,
    })
