# Generated by Django 4.1.7 on 2023-03-27 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0010_rename_data_logs_get_data_logs_post_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='get_data',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='logs',
            name='post_data',
        ),
    ]