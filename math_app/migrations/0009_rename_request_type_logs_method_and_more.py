# Generated by Django 4.1.7 on 2023-03-27 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0008_remove_logs_headers_logs_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='request_type',
            new_name='method',
        ),
        migrations.RenameField(
            model_name='logs',
            old_name='time',
            new_name='timestamp',
        ),
    ]