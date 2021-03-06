# Generated by Django 3.0.8 on 2020-10-03 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0019_dialogphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupchat',
            name='chat_image',
        ),
        migrations.CreateModel(
            name='GroupChatMainPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_image', models.ImageField(blank=True, null=True, upload_to='chat/main_chat_image', verbose_name='Main photo of chat')),
                ('group_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.GroupChat')),
            ],
            options={
                'verbose_name': 'GroupChatPhoto',
                'verbose_name_plural': 'GroupChatMessages',
            },
        ),
    ]
