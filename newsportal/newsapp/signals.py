from django.contrib.sites import requests
from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import get_object_or_404

from .models import *


@receiver(m2m_changed, sender=PostCategory)
def send_sub_mail(sender, instance, *args, **kwargs):

    title_ = instance.id
    cat = Category.objects.all().values_list('name', "subscribers")
    sub = instance.postCategory.values_list("name", flat=True)

    for n, m in cat:
        if m is not None:
            #print('n:', n)
            #print('m:', m.get_absolute_url())
            for c in sub:
                #print('c:', c)
                if n == c:
                    send_mail(subject=f"{instance.title}",
                              message=f"Здравствуй,{User.objects.get(pk=m)}."
                                      f" Новая статья в твоём любимом разделе! {c} \n "
                                      f"Заголовок статьи: {instance.title} \n"
                                      f" Текст статьи: {instance.text[:50]} \n"
                              
                                      f'Перейти на новость: http://127.0.0.1:8000/news/{title_}',

                              from_email='stexeserver@yandex.ru',
                              recipient_list=[f'{User.objects.get(pk=m).email}'],
                              )
