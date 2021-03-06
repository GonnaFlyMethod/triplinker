# Generated by Django 3.0.8 on 2020-09-10 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_places', '0009_place_timestamp'),
        ('journeys', '0012_auto_20200910_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='place_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_places', to='trip_places.Place'),
        ),
    ]
