# Generated by Django 3.0.8 on 2020-08-27 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TLAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=15, verbose_name='First name')),
                ('second_name', models.CharField(blank=True, max_length=15, verbose_name='Second name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=2, verbose_name='Sex')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('country', models.CharField(blank=True, choices=[('BY', 'Belarus')], max_length=25, verbose_name='Country')),
                ('place_of_work', models.CharField(blank=True, max_length=70, verbose_name='Place of work')),
                ('short_description', models.CharField(blank=True, max_length=500, verbose_name='Short description')),
                ('hobbies', models.CharField(blank=True, max_length=250, verbose_name='Hobbies')),
                ('vkontakte', models.URLField(blank=True, null=True, verbose_name='VKontakte')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('can_get_message_from', models.CharField(choices=[('Friends', 'Friends only'), ('All', 'All users')], default='All', max_length=12, verbose_name='Get messages from')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('followers', models.ManyToManyField(blank=True, related_name='followers_of_user', to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('people_which_follow', models.ManyToManyField(blank=True, related_name='people_which_follow_cur_usr', to=settings.AUTH_USER_MODEL)),
                ('strangers', models.ManyToManyField(blank=True, related_name='messages_strangers', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friend request',
                'verbose_name_plural': 'Friend requests',
            },
        ),
    ]
