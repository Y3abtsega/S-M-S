# Generated by Django 2.2.2 on 2023-09-10 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0006_auto_20230910_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='name',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='name',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='name',
            name='user_permissions',
        ),
    ]
