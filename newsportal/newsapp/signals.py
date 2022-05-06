from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import send_mail
from django.shortcuts import redirect

from .models import *


@receiver(m2m_changed, sender=PostCategory)
def post(sender, instance, *args, **kwargs):
    users = Category.objects.filter(pk=instance.postCategory.all()).values("subscribers")
    for i in users:
        send_mail(
            subject=f"{instance.title}",
            message=f"Здравствуй, {User.objects.get(pk=i['subscribers']).username}."
                    f" Новая статья в твоём любимом разделе! \n Заголовок статьи: {instance.title} \n"
                    f" Текст статьи: {instance.text[:50]}",
            from_email='utochkin.rcoko92@yandex.ru',
            recipient_list=[User.objects.get(pk=id['subscribers']).email]
        )
        return redirect('/news/')
