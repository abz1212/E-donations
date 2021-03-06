# Generated by Django 3.0.8 on 2020-08-20 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to=settings.AUTH_USER_MODEL, verbose_name='donor'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='sponsors', to='donations.Acceptor', verbose_name='acceptor'),
        ),
        migrations.AddField(
            model_name='organ',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organs', to=settings.AUTH_USER_MODEL, verbose_name='donor'),
        ),
        migrations.AddField(
            model_name='blood',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloods', to=settings.AUTH_USER_MODEL, verbose_name='donor'),
        ),
    ]
