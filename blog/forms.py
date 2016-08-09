from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostCreateForm(forms.ModelForm):
    tags = forms.CharField(label='tags', max_length=600)
    class Meta: 
        model = Post
        fields = ['title', 'text']
    
    def clean_tags(self):
        tags = self.cleaned_data['tags']
        tags = tags.split(',')
        if len(tags) == 0:
            raise ValidationError('No tags specified')
        return tags
