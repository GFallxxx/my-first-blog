from django import forms
from .models import Post, BlogComment

class PostForm (forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm (forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ('author', 'text')

