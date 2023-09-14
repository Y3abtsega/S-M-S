# Generated by Django 2.2.2 on 2023-09-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_auto_20230910_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='fullname',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='name',
            name='username',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
