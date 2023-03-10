# Generated by Django 3.0.7 on 2022-12-25 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20221225_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100)),
                ('assets_id', models.PositiveIntegerField(null=True)),
                ('accept_reason', models.CharField(max_length=100)),
                ('date_of_activity', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
