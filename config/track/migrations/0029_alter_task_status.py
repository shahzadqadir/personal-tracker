# Generated by Django 4.1.4 on 2022-12-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0028_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not-started', 'not-started'), ('ongoing', 'ongoing'), ('completed', 'completed')], default='not-started', max_length=50),
        ),
    ]
