from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(template_name='newsapp/news.html'), name='news'),
    path('news/<int:pk>', NewsDetail.as_view(template_name='newsapp/new.html'), name='new'),
    path('news/search/', NewsList.as_view(template_name='newsapp/search.html'), name='news/search/'),
    path('create/', NewsCreate.as_view(template_name='newsapp/news_edit.html'), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(template_name='newsapp/news_edit.html'), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(template_name='newsapp/news_delete.html'), name='news_delete'),
    path('articles/', ArticlesList.as_view(template_name='newsapp/articles.html'), name='articles'),
    path('articles/<int:pk>', ArticlesDetail.as_view(template_name='newsapp/article.html'), name='article'),
    path('createA/', ArticlesCreate.as_view(template_name='newsapp/articles_edit.html'), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(template_name='newsapp/articles_edit.html'),
         name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(template_name='newsapp/articles_delete.html'),
         name='articles_delete'),
    path('<int:pk>/subscribe/', add_subscribe, name='subscribe'),
    path('subscribers/', ArticlesList.as_view(template_name='newsapp/subscribers.html'),
         name='subscribers')
]
