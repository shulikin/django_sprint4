from django import forms

from .models import Post, User, Comment


class PostForm(forms.ModelForm):
    text = forms.CharField(
        label="Текст",
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
        label="Комментарий",
        widget=forms.Textarea,
    )

    class Meta:
        model = Comment
        fields = ('text',)
