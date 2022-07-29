from .models import Comment, Post, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'slug', 'content', 'featured_image', 'excerpt', 'status')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'name', 'email_address', 'phone', 'message')
