# Generated by Django 3.1.4 on 2021-01-14 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20210114_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='thumbnail',
        ),
    ]