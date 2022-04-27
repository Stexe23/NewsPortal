from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    '''Наследовать форму от модели'''
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'address']
