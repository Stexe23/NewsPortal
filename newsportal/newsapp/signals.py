from django.core.serializers import json
from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from .tasks import send_new_news

from .models import *


@receiver(m2m_changed, sender=PostCategory)
def send_sub_mail(sender, instance, *args, **kwargs):
    send_new_news.delay(instance.id, instance.title, instance.text)
