# Generated by Django 4.2.5 on 2023-10-06 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0013_grades_studentname_subjects_delete_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='studentname',
            new_name='student',
        ),
    ]