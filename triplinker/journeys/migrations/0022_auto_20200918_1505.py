# Generated by Django 3.0.8 on 2020-09-18 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journeys', '0021_merge_20200916_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='participants',
            field=models.ManyToManyField(blank=True, through='journeys.Participant', to=settings.AUTH_USER_MODEL, verbose_name='Particapants of the journey'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='journey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journeys.Journey'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
