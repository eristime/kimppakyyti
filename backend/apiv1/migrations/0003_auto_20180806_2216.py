# Generated by Django 2.1 on 2018-08-06 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0002_auto_20180806_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='ride_ended',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ride',
            name='passengers',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL, verbose_name='passengers'),
        ),
    ]
