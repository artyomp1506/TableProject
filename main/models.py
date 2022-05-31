from django.db import models


class Student(models.Model):
    name_ru = models.CharField(max_length=255, verbose_name='Фио на русском языке')
    name_en = models.CharField(max_length=255, verbose_name='Фио на английском языке')
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, null=True, verbose_name='Пол')
    country = models.CharField(max_length=255, verbose_name='Страна')
    number_doc = models.BigIntegerField(blank=True, verbose_name="Номер документа")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения"),
    #user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.name_ru


class Gender(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
