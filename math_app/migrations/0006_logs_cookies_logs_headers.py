# Generated by Django 4.1.7 on 2023-03-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0005_remove_logs_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='cookies',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='headers',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
