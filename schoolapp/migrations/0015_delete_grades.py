# Generated by Django 4.2.5 on 2023-10-06 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0014_rename_studentname_subjects_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Grades',
        ),
    ]
