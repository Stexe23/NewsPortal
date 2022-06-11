from celery import shared_task
from celery.schedules import crontab
from django.contrib.auth import get_user_model
from django.contrib.sites import requests
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import request

import newsportal
from .models import *
import datetime


@shared_task
def send_new_news(name_id):
    UserModel = get_user_model()
    user = User.objects.all().values_list("username")
    title_ = Post.objects.all().values('pk')
    text = Post.text
    cat = Category.objects.all().values_list('name', 'subscribers')
    sub = Category.objects.all().values_list('name', flat=True)

    print(cat)

    for n, m in cat:
        if m != None:
            print('Категория подписки:', n)
            print('Id пользователя:', m)

            for c in sub:
                print('Категория выбора:', c)
                if n is c:
                    send_mail(subject=f"{title_}",
                              message=f"Здравствуй,{user}. \n Новая статья в твоём любимом разделе! {c}. \n Заголовок статьи: {title_} \n Текст статьи: {text[:50]} \n Перейти на новость: http://127.0.0.1:8000/news/{title_}",
                              from_email='stexeserver@yandex.ru',
                              recipient_list=[f'{user.email}'],
                              )


@shared_task
def send_news_week():
    newsportal.conf.beat_schedule = {
        'action_every_monday_8am': {
            'task': 'action',
            'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        },
    }
