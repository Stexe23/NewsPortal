from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import *


@shared_task
def send_new_news(name_id, title_, text_):
    user_u = Category.objects.all().values_list('name', 'subscribers')
    p = Post.objects.get(id=name_id)
    cat_ = p.postCategory.all().values_list('name', flat=True)

    for s in cat_:
        for c, u in user_u:
            if (u is not None) and (c == s):
                send_mail(
                        subject=f'{title_}',
                        message=f"Здравствуй, {User.objects.get(pk=u)}! \n Новая статья в твоем любимом разделе {s}!\n Заголовок статьи: {title_} \n Текст статьи: {text_[:50]} ... \n Полный текст по ссылке: http://127.0.0.1:8000/news/{name_id}",
                        from_email='stexeserver@yandex.ru',
                        recipient_list=[f'{User.objects.get(pk=u).email}'],
                )


@shared_task
def send_news_week():
    for post in Post.objects.filter(created__gt=(datetime.date.today() - datetime.timedelta(minutes=120))):
        for cat in PostCategory.objects.filter(post=post):
            for subscribe in Category.objects.filter(category=cat.category):
                msg = EmailMultiAlternatives(
                    subject=post.title,
                    body=post.contents,
                    from_email='stexeserver@yandex.ru',
                    to=[subscribe.subscriber.email],
                )
                html_content = render_to_string(
                    'weeklysubscribeletter.html',
                    {
                        'new': post,
                        'recipient': subscribe.subscriber
                    }
                )

                msg.attach_alternative(html_content, "text/html")
                msg.send()



