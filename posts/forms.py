from django import forms
from location_field.forms.plain import PlainLocationField

from posts.models import Post


class PostForm(forms.ModelForm):
    location = PlainLocationField(based_fields=['city'], initial='-22.2876834,-49.1607606')

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'city', 'region', 'location']
