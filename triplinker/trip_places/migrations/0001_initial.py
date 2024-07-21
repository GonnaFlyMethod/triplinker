# Generated by Django 3.0.8 on 2020-08-27 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_place', models.CharField(max_length=50, verbose_name='Name of place')),
                ('type_of_place', models.CharField(choices=[('TownCity', 'Town or city'), ('NatureObj', 'Object of nature')], max_length=30, verbose_name='Type of place')),
                ('place_description', models.CharField(blank=True, max_length=500, verbose_name='Short description')),
                ('place_pic', models.ImageField(blank=True, null=True, upload_to='public/media/')),
                ('location', models.CharField(choices=[('BY', 'Belarus')], max_length=25, verbose_name='The location of place')),
                ('rating', models.CharField(choices=[('1', 'One star'), ('2', 'Two stars'), ('3', 'Three stars'), ('4', 'Four stars'), ('5', 'Five stars')], max_length=25, verbose_name='The rating of place')),
                ('who_added_place_on_site', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_who_added_place_on_site', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
    ]