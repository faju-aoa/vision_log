# Generated by Django 5.1.7 on 2025-03-17 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vision_logs', '0002_rename_entry_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={},
        ),
        migrations.RemoveField(
            model_name='content',
            name='date_added',
        ),
    ]
