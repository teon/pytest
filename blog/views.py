from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class PostListView(ListView):
    #model = Post
    queryset = Post.objects.filter(published_date__lte = timezone.now())
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'text']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.created_date = timezone.now()
        form.instance.published_date = timezone.now()
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostEditView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'text']
    success_url = '/'
    

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

