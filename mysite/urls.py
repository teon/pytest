from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login', kwargs={'template_name': 'auth/login.html'}),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page':'/'}),
    url(r'', include('blog.urls')),

]
