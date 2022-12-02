from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    username = models.CharField(max_length=30, unique=True, null=False, help_text='Логин',
                                error_messages={'unique': "Такой пользователь уже существует!"})
    avatar = models.ImageField(upload_to='images/avatars/', verbose_name='Аватарка')
    user_info = models.CharField(max_length=40, null=True, help_text='Информация')

    def __str__(self):
        return self.username


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.today(), null=False, verbose_name='Дата')
    life_time = models.DateTimeField(default=datetime.today() + timedelta(days=1), verbose_name='Время жизни', null=False)
    full_info = models.CharField(max_length=50, null=False, help_text='полное описание')
    short_info = models.CharField(max_length=25, null=False, help_text='краткое описание')
    question_image = models.ImageField(upload_to='images/questions/', verbose_name='картинка')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)


    def procent(self):
        return round(100 * self.votes / self.question.votes)


    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    votes = models.IntegerField(default=1, verbose_name='Количество голосов')

    def __str__(self):
        return f'{self.question} - {self.user}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

