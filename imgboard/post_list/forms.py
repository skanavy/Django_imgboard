from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'thread')
        labels = {
            'title': _('Заголовок'),
            'text': _('Текст поста'),
            'image': _('Картинка'),
            'thread': _('тред'),
        }
