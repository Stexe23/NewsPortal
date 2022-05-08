import requests
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import send_mail
from django.http import request, HttpRequest
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .models import *


@receiver(m2m_changed, sender=PostCategory)
def post(sender, instance, *args, **kwargs):
    us_c = Category.objects.all().values_list("subscribers", flat=True)
    cat = Category.objects.all().values_list('name', "subscribers")
    sub = instance.postCategory.values_list("name", flat=True)
    #print(us_c)
    #print(cat)
    #print(sub)
    for n, m in cat:
        if m is not None:
            #print('n:', n)
            #print('m:', m)
            for c in sub:
                #print('c:', c)
                if n == c:
                    send_mail(subject=f"{instance.title}",
                              message=f"Здравствуй,{User.objects.get(pk=m)}."
                                      f" Новая статья в твоём любимом разделе! {c} \n "
                                      f"Заголовок статьи: {instance.title} \n"
                                      f" Текст статьи: {instance.text[:50]}",
                              from_email='stexeserver@yandex.ru',
                              recipient_list=[f'{User.objects.get(pk=m).email}'],
                      )
