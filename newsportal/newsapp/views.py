import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from .forms import *
from .models import *
from .filters import NewsFilter, ArticleFilter


class NewsList(ListView):
    model = Post
    context_object_name = 'news'
    queryset = Post.objects.all().order_by("-dateCreation")
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список статей
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    context_object_name = 'new'


class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    model = Post
    permission_required = ('post.add_news',)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    form_class = NewsForm
    model = Post
    permission_required = ('post.change_news',)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    queryset = Post.objects.all()
    success_url = reverse_lazy('news')
    permission_required = ('news.delete_post',)


class ArticlesList(ListView):
    model = Category
    context_object_name = 'articles'
    queryset = Category.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ArticlesDetail(DetailView):
    model = Category
    context_object_name = 'article'


class ArticlesCreate(CreateView):
    success_url = reverse_lazy('category.add_articles')
    form_class = ArticlesForm
    model = Category


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('category.change_articles',)
    form_class = ArticlesForm
    model = Category

    def get_object(self, **kwargs):
        id_ = self.kwargs.get('pk')
        return Category.objects.get(pk=id_)


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('category.delete_articles',)
    model = Category
    success_url = reverse_lazy('articles')


class SubscribersList(ListView):
    model = Category
    form_class = ArticlesForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        sub = Category.objects.all()
        us = User.objects.all().values_list("subscribers", flat=True)
        us_c = Category.objects.all().values_list("subscribers", flat=True)
        cat = Category.objects.all().values_list('name', "subscribers")
        print('sub:', sub)
        print('us:', us)
        print('us_c:', us_c)
        print('cat:', cat)
        context['categories'] = Category.objects.all().values_list('name', "subscribers")
        return context


def group_gains_perms(request, group_name):
    group = get_object_or_404(Group, name='authors')
    group.has_perm('news.add_post', 'news.change_post', 'news.delete_post')
    content_type = ContentType.objects.get_for_model(Post)
    perm_c = Permission.objects.get(
        codename='news.add_post',
        name='Create news',
        content_type=content_type,
    )

    perm_e = Permission.objects.get(
        codename='news.change_post',
        name='Edit news',
        content_type=content_type,
    )

    perm_d = Permission.objects.create(
        codename='news.delete_post',
        name='Delit news',
        content_type=content_type,
    )

    group.group_permissions.add(perm_c, perm_e, perm_d)
    group.has_perm('news.add_post', 'news.change_post', 'news.delete_post')
    group = get_object_or_404(Group, name='authors')
    group.has_perm('news.add_post', 'news.change_post', 'news.delete_post')
    return requests.request(group)


@login_required
def add_subscribe(request, pk):
    a = request.user
    a.save()
    b = Category.objects.get(id=pk)
    b.subscribers.add(a)
    return redirect('/subscribers/')


@login_required
def del_subscribe(request, pk):
    a = request.user
    a.save()
    b = Category.objects.all().values_list('subscribers')
    print(b)
    b.subscribers.delete(a)
    return redirect('/subscribers/')
