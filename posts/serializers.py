import re
from rest_framework import serializers
from .models import Post, Tag
from django.contrib.auth.models import User


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = ('id', 'username', 'password', 'posts')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class PostSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SerializerMethodField(read_only=True)
    coma_separated_tags = serializers.CharField(max_length=100, write_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    def validate_coma_separated_tags(self, value):
        regex = re.compile("\w+(,\w+)*")
        if not regex.match(value):
            raise serializers.ValidationError("Tags must be separated with comas, without whitespaces")

        return value

    def get_tags(self, obj):
        tag_list = []
        for tag in obj.tags.all():
            tag_list.append(tag.name)
        return ','.join(tag_list)

    # @transaction.atomic
    def create(self, validated_data):
        tags_data = validated_data.pop('coma_separated_tags')
        post = super().create(validated_data)
        for tag in tags_data.split(","):
            model = Tag()
            model.name = tag
            model.save()
            post.tags.add(model)

        return post

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'text', 'created_date', 'published_date', 'tags', 'coma_separated_tags')
