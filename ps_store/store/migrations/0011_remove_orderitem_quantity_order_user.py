# Generated by Django 4.1.4 on 2022-12-28 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0010_order_vk_or_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказы'),
        ),
    ]
