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


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'newsapp/news_edit.html'


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'newsapp/news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'newsapp/news_delete.html'
    success_url = reverse_lazy('news')


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
    form_class = ArticlesForm
    model = Category
    template_name = 'newsapp/articles_edit.html'
    success_url = reverse_lazy('articles')


class ArticlesUpdate(UpdateView):
    form_class = ArticlesForm
    model = Category
    template_name = 'newsapp/articles_edit.html'


class ArticlesDelete(DeleteView):
    model = Category
    template_name = 'newsapp/articles_delete.html'
    success_url = reverse_lazy('articles')

