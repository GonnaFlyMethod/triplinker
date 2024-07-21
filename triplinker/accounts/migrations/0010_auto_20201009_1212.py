# Generated by Django 3.0.8 on 2020-10-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userphotogallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalQualities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualities', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Quality',
                'verbose_name_plural': 'Qualities',
            },
        ),
        migrations.AddField(
            model_name='tlaccount',
            name='qualities',
            field=models.ManyToManyField(to='accounts.PersonalQualities'),
        ),
    ]