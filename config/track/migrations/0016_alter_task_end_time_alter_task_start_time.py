# Generated by Django 4.1.1 on 2022-10-02 05:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("track", "0015_alter_task_end_time_alter_task_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="end_time",
            field=models.TimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="start_time",
            field=models.TimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
    ]