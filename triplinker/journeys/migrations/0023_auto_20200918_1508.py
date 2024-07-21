# Generated by Django 3.0.8 on 2020-09-18 15:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journeys', '0022_auto_20200918_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='participants',
            field=models.ManyToManyField(blank=True, default=None, through='journeys.Participant', to=settings.AUTH_USER_MODEL, verbose_name='Particapants of the journey'),
        ),
    ]
