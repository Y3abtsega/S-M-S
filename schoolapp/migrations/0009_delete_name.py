# Generated by Django 4.2.5 on 2023-09-19 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0008_remove_name_fullname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Name',
        ),
    ]