# Generated by Django 4.1.3 on 2022-12-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_posts_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
    ]
