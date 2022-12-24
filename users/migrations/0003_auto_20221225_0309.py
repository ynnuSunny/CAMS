# Generated by Django 3.0.7 on 2022-12-24 21:09

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221224_2014'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stuff',
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('staff', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('MANAGER', 'Manager'), ('STAFF', 'Staff'), ('EMPLOYEE', 'Employee')], max_length=50),
        ),
    ]