from django.contrib.auth.models import Group, User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(BaseRegisterForm, self).save()
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        print('Custom group works!')
        return user

