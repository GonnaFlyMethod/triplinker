# Generated by Django 3.0.8 on 2020-08-29 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trip_places', '0004_photo_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ('-timestamp',), 'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AddField(
            model_name='photo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_of_photo', to=settings.AUTH_USER_MODEL),
        ),
    ]
