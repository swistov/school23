from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Pupil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['user']

    def __str__(self):
        return self.user.username


class Evaluations(models.Model):
    user = models.OneToOneField(Pupil, on_delete=models.CASCADE)
    eval = models.CharField(max_length=50, null=False, unique=False, blank=False, verbose_name='Задание')
    answer = models.CharField(max_length=3, unique=False, null=False, verbose_name='Ответ')
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField()

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['user']

    def __str__(self):
        return self.eval
