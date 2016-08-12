import django_filters
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostFilter(filters.FilterSet):
    tag = django_filters.CharFilter(name="tags__name")
    title = django_filters.CharFilter(name="title", lookup_expr='contains')

    class Meta:
        model = Post
        fields = ['title', 'tag']


class PostViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
