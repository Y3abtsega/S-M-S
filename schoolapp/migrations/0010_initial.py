# Generated by Django 4.2.5 on 2023-10-05 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schoolapp', '0009_delete_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(blank=True, max_length=2000, unique=True)),
                ('cl', models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'), ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten'), ('eleven', 'eleven'), ('twelve', 'twelve')], default='one', max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ManyToManyField(to='schoolapp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='TakenCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('mid_exam', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('quiz', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('final_exam', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], default='F', max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]