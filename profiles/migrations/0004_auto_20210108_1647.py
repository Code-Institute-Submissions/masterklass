# Generated by Django 3.1.4 on 2021-01-08 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0005_auto_20210108_1647'),
        ('profiles', '0003_auto_20210108_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='active',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='plan',
            field=models.OneToOneField(blank=True, limit_choices_to={'active': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase.plan'),
        ),
    ]
