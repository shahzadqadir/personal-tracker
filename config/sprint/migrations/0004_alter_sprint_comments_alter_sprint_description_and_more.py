# Generated by Django 4.1.4 on 2023-02-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0003_alter_sprint_comments_alter_sprint_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='comments',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='status',
            field=models.CharField(choices=[('not-started', 'Not Started'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'cancelled')], default='not-started', max_length=50),
        ),
    ]
