from django.contrib.auth import authenticate, login  # , logout
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bookmarkapp.models import Bookmark, Click
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
# from django.views.generic import DetailView
from bookmarkapp.forms import BookmarkForm, EditBookmarkForm
from datetime import datetime


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


class UserDetailView(ListView):
    """Used to view a User and their list of bookmarks"""
    #   model = User
    template_name = 'bookmarkapp/user_detail.html'
    context_object_name = 'bookmarks'
    paginate_by = 10

    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])
        preload = self.user.bookmark_set.all()
        return preload.order_by('-timestamp')
    # def get_queryset(self):
    #
    #     return User.objects.get(pk=pk).bookmark_set.all()

    # queryset = Bookmark.objects.get(author=self.user)

    # def get_context_data(self, **kwargs):
    #     context = super(UserDetailView, self).get_context_data(**kwargs)
    #     return context


class AllBookmarkView(ListView):
    """Used to view a User and their list of bookmarks"""
    #   model = User
    template_name = 'bookmarkapp/index.html'
    context_object_name = 'bookmarks'
    paginate_by = 20

    def get_queryset(self):
        preload = Bookmark.objects.all()
        return preload.order_by('-timestamp')


def short_to_long(request, short_url):
    bookmark = get_object_or_404(Bookmark, short_url=short_url)
    try:
        click = Click(bookmark=bookmark, clicker=request.user)
    except:
        click = Click(bookmark=bookmark)
    click.save()
    return redirect(bookmark.original_url)


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


@login_required
def addbookmark(request):
    form_class = BookmarkForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            original_url = request.POST.get('original_url', '')
            author = request.user
            # short_url = Bookmark.objects.create_short_url('original_url')

            bookmark = Bookmark(
                title=title,
                description=description,
                original_url=original_url,
                author=author
            )
            bookmark.save()
            bookmark.short_url = bookmark.create_short_url(original_url)
            bookmark.save()

            return redirect('addbookmark')

    return render(request, 'bookmarkapp/addbookmark.html', {
        'form': form_class,
    })


@login_required
def editbookmark(request, uid):
    form_class = EditBookmarkForm
    if Bookmark.objects.get(pk=uid).author != request.user:
        return redirect('home_page')

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():

            try:
                row = Bookmark.objects.get(pk=uid)
                if request.POST['title']:
                    row.title = request.POST['title']
                if request.POST['description']:
                    row.description = request.POST['description']
            except:
                pass
            row.save()

            return redirect('user_detail', request.user.pk)

    return render(request, 'bookmarkapp/editbookmark.html', {
        'form': form_class,
    })


@login_required
def deletebookmark(request, uid):
    if Bookmark.objects.get(pk=uid).author != request.user:
        return redirect('home_page')
    else:
        Bookmark.objects.get(pk=uid).delete()
        return redirect('user_detail', request.user.pk)
    # return render(request, 'bookmarkapp/deletebookmark.html', {
    #     'form': form_class,
    # })
