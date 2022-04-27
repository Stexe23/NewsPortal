from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    GENDER_CHOICE = (
                 ('мужской', ' '),
                 ('женщина', ' ')
    )
    nick_name = models.CharField (max_length = 20, verbose_name = 'nickname', null = True, blank = True)
    mobile = models.CharField (max_length = 11, verbose_name = 'phone', null = True, blank = True)
    адрес = models.CharField (max_length = 200, verbose_name = 'address', null = True, blank = True)

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username
