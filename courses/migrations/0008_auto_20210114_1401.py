# Generated by Django 3.1.4 on 2021-01-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_merge_20210108_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(default='default-image.png', upload_to='media'),
        ),
    ]
