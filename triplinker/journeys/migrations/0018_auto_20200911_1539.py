# Generated by Django 3.0.8 on 2020-09-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0017_auto_20200911_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Description of activity'),
        ),
    ]