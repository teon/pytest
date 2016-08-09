from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', login_required(views.PostCreateView.as_view()), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', login_required(views.PostEditView.as_view()), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', login_required(views.PostDeleteView.as_view()), name='post_remove'),
    url(r'^register/$', views.UserCreateView.as_view() , name='register'),
]
