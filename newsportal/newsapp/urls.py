from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(template_name='newsapp/news.html'), name='news'),
    path('news/<int:pk>', NewsDetail.as_view(template_name='newsapp/new.html'), name='new'),
    path('news/search/', NewsList.as_view(template_name='newsapp/search.html'), name='news/search/'),
    path('create/', NewsCreate.as_view(template_name='news_edit.html'), name='news_create'),
    path('<int:pk>/edit', NewsUpdate.as_view(template_name='newsapp/news_edit.html'), name='news_edit'),
    path('<int:pk>/delete', NewsDelete.as_view(template_name='newsapp/news_delete.html'), name='news_delete'),

    path('articles/', ArticlesList.as_view(template_name='newsapp/articles.html'), name='articles'),
    path('articles/<int:pk>', ArticlesDetail.as_view(template_name='newsapp/article.html'), name='article'),
    path('create/', ArticlesCreate.as_view(template_name='articles_edit.html'), name='articles_create'),
    path('<int:pk>/edit/', ArticlesUpdate.as_view(template_name='newsapp/articles_edit.html'), name='articles_edit'),
    path('<int:pk>/delete/', ArticlesDelete.as_view(template_name='newsapp/articles_delete.html'),
         name='articles_delete'),
]
