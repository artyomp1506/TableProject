# Generated by Django 3.2 on 2022-06-10 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255, verbose_name='Фио на русском языке')),
                ('name_en', models.CharField(max_length=255, verbose_name='Фио на английском языке')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('born_city', models.CharField(max_length=255, verbose_name='Город рождения')),
                ('live_city', models.CharField(max_length=255, verbose_name='Город проживания')),
                ('number_doc', models.BigIntegerField(blank=True, verbose_name='Номер документа')),
                ('enroll', models.BooleanField(default=False, verbose_name='Зачислен')),
                ('enrollment_number', models.BigIntegerField(blank=True, verbose_name='Номер приказа о зачислении')),
                ('deduction_number', models.BigIntegerField(blank=True, verbose_name='Номер приказа об отчислении')),
                ('education_form_type', models.CharField(choices=[('online', 'Online'), ('traditional', 'Традиционная'), ('hybrid', 'Смешанная')], default='online', max_length=255, verbose_name='Форма обучения')),
                ('application_from_type', models.CharField(choices=[('self', 'сам'), ('other', '3-е лицо')], default='self', max_length=255, verbose_name='Форма подачи заявления')),
                ('time_birth', models.DateTimeField(auto_now_add=True, verbose_name='Дата рождения')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.gender', verbose_name='Пол')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
