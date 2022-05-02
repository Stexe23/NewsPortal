from django import forms
from django.core.exceptions import ValidationError

from .models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'categoryType',
            'postCategory',
            'text',
        )
        labels = {'categoryType': 'Attribute', 'postCategory': 'Teg/Articles'}

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError({
                "text": "Статья не может быть менее 20 символов."
            })

        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Статья не должна быть идентично названию."
            )

        return cleaned_data


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
