# Generated by Django 3.2.9 on 2021-11-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_student_student_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registartion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
            ],
        ),
    ]