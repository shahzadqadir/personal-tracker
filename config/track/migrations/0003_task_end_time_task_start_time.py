# Generated by Django 4.1.1 on 2022-09-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_quotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
