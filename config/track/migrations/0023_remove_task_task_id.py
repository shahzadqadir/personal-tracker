# Generated by Django 4.1.1 on 2022-11-10 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0022_task_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_id',
        ),
    ]
