# Generated by Django 3.0.8 on 2020-09-03 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0004_auto_20200902_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journey',
            old_name='data_of_end',
            new_name='date_of_end',
        ),
    ]
