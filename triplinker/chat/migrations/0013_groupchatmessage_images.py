# Generated by Django 3.0.8 on 2020-09-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_groupchatmessage_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchatmessage',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='chat/pictures_of_messages', verbose_name='Picture of message'),
        ),
    ]
