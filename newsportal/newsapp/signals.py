import signal

from django.contrib.sites import requests
from django.db.models.signals import m2m_changed
from django.db.models import signals
from django.dispatch import receiver  # импортируем нужный декоратор
from .tasks import send_new_news
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import get_object_or_404

from .models import *


@receiver(m2m_changed, sender=PostCategory)
def send_sub_mail(sender, instance, *args, **kwargs):
    send_new_news.delay(instance.id)



#signals.m2m_changed.connect(send_sub_mail, sender=PostCategory)

