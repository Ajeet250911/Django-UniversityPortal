# Generated by Django 3.2.9 on 2021-11-27 06:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=40)),
                ('student_name', models.CharField(max_length=40)),
                ('student_email', models.EmailField(max_length=50)),
                ('student_phone', models.CharField(max_length=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.course')),
            ],
        ),
    ]
