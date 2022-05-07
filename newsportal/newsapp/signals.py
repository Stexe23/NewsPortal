from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import redirect

from .models import *


@receiver(m2m_changed, sender=PostCategory)
def post(sender, instance, *args, **kwargs):
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    if action == "post_add":
        if 1 not in pk_set:
            pk_set.update([1])
            send_mail(
                subject=f"{instance.title}",
                html_message=f"Здравствуй, {instance.username}."
                             f" Новая статья в твоём любимом разделе! \n Заголовок статьи: {instance.title} \n"
                             f" Текст статьи: {instance.text[:50]}",
                from_email='stexeserver@yandex.ru',
                recipient_list=[f'{instance.username.email}']
            )
        return redirect('/news/')
