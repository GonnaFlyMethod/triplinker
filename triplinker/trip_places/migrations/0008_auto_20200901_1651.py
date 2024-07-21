# Generated by Django 3.0.8 on 2020-09-01 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trip_places', '0007_auto_20200830_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_feedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_feedback', to='trip_places.Place'),
        ),
    ]
