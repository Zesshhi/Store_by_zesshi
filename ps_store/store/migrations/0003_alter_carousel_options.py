# Generated by Django 4.1.3 on 2022-12-10 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_carousel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['title'], 'verbose_name': 'Главная слайдер', 'verbose_name_plural': 'Слайдеры'},
        ),
    ]
