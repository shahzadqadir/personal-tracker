# Generated by Django 4.1.1 on 2022-11-10 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0023_remove_task_task_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='content_id',
            new_name='object_id',
        ),
    ]
