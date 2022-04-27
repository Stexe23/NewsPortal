from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
