from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Post, User, Comment


@deconstructible
class RussCharsValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "

    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Допускаются только русские символы, дефис и пробел."

    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(
                self.message,
                code=self.code,
                params={'value': value}
            )


class PostForm(forms.ModelForm):
    text = forms.CharField(
        label="Текст",
        validators=[
            RussCharsValidator(),
        ],
        widget=forms.Textarea,
    )

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'datetime-local'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        # label="Комментарий",
        validators=[
            RussCharsValidator(),
        ],
        widget=forms.Textarea,
    )

    class Meta:
        model = Comment
        fields = ('text',)
