from django.http import HttpResponse
from .models import Post, Tag
from django.utils import timezone
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import PostCreateForm
from django.db.models import Q
from django.views.generic.edit import FormView

class PostListView(ListView):
    def get(self, request, *args, **kwargs):
        self.queryset = Post.objects.filter(~Q(published_date = None))
        self.template_name = 'blog/post_list.html'
        tag = request.GET.get('tag', None)
        if tag:
            self.queryset = self.queryset.filter(tags__name = tag)
        name = request.GET.get('name', None)
        if name:
            self.queryset = self.queryset.filter(title__contains = name)

        return render(request, self.template_name, {'post_list': self.queryset})

class PostDetailView(DetailView):
    model = Post

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

class PostCreateView(FormView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostCreateForm
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.created_date = timezone.now()
        form.instance.published_date = timezone.now()
        form.instance.author = self.request.user
        tags = form.cleaned_data['tags']
        self.object = form.save()
        for tag in tags:
            model = Tag()
            model.name = tag
            model.save()
            self.object.tags.add(model)

        return super(PostCreateView, self).form_valid(form)

class PostEditView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'text']
    success_url = '/'
    

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

