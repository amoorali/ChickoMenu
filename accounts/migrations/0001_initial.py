# Generated by Django 4.1 on 2023-05-17 08:23

import accounts.models
from django.db import migrations, models
import django.utils.timezone
import django_jalali.db.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(db_index=True, max_length=60, unique=True, verbose_name='نام کاربری')),
                ('first_name', models.CharField(blank=True, max_length=20, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='نام خانوادگی')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل شما')),
                ('date_joined', django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ عضویت')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_location, verbose_name='عکس پروفایل')),
                ('address', models.TextField(blank=True, max_length=420, null=True, verbose_name='address')),
                ('post_code', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='post code')),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'پروفايل كاربر',
                'verbose_name_plural': 'پروفايل كاربرها',
            },
        ),
    ]