from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from newsapp.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/apage/'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        Author.objects.create(authorUser=user)
        authors_group.user_set.add(user)
    return redirect('/apage/')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'newsportal/index.html'


@method_decorator(login_required)
def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_not_authors'] = not self.request.User.groups.filter(name='authors').exists()
    context['is_authors'] = self.request.User.groups.filter(name='authors').exists()
    return context


