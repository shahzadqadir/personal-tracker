# Generated by Django 4.1.4 on 2022-12-16 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0029_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_completed',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
