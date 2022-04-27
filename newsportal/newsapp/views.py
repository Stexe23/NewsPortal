from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
    permission_required = ('news.add_post',)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    form_class = NewsForm
    model = Post


class NewsDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    queryset = Post.objects.all()
    success_url = reverse_lazy('news')
    permission_required = ('new.delete_post',)


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


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    form_class = ArticlesForm
    model = Category
    success_url = reverse_lazy('articles')


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    form_class = ArticlesForm
    model = Category
    permission_required = ('article.change_category',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Category.objects.get(pk=id)


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('articles')
    permission_required = ('article.delete_category',)

