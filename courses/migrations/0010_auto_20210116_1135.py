# Generated by Django 3.1.4 on 2021-01-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_remove_lesson_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
    ]