from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'location', 'pub_date', 'image')
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'category': 'Категория',
            'location': 'Местоположение',
            'pub_date': 'Дата публикации',
            'image': 'Изображение',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст комментария',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }


class UserProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Убираем поле password
        if 'password' in self.fields:
            self.fields.pop('password')
