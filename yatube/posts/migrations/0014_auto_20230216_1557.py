# Generated by Django 2.2.16 on 2023-02-16 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20230216_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='блогер'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='подписчик'),
        ),
    ]
