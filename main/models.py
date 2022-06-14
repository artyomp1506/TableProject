from django.contrib.auth import get_user_model
from django.db import models
from .constants import education_form, application_from
User = get_user_model()


class Student(models.Model):
    name_ru = models.CharField(max_length=255, verbose_name='ФИО на русском языке')
    name_en = models.CharField(max_length=255, verbose_name='Фио на английском языке')
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, null=True, verbose_name='Пол')
    country = models.CharField(max_length=255, verbose_name='Страна')
    born_city = models.CharField(max_length=255, verbose_name='Город рождения')
    live_city = models.CharField(max_length=255, verbose_name='Город проживания')
    number_doc = models.BigIntegerField(blank=True, verbose_name="Номер документа")
    enroll = models.BooleanField(default=False, verbose_name="Зачислен")
    enrollment_number = models.BigIntegerField(blank=True, verbose_name="Номер приказа о зачислении")
    deduction_number = models.BigIntegerField(blank=True, verbose_name="Номер приказа об отчислении")
    education_form_type = models.CharField(max_length=255, choices=education_form, default="online", verbose_name="Форма обучения")
    application_from_type = models.CharField(max_length=255, choices=application_from, default="self", verbose_name="Форма подачи заявления")
    time_birth = models.DateTimeField(auto_now_add=True, verbose_name="Дата рождения")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.name_ru


class Gender(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='Имя пользователя')
    password = models.CharField(max_length=12, verbose_name='Пароль')
    email = models.CharField(blank=True, max_length=20, verbose_name='e-mail')
