# Generated by Django 3.2.7 on 2021-11-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20211101_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicedata',
            name='cpu_totalavg_idle_percentage',
        ),
        migrations.RemoveField(
            model_name='devicedata',
            name='cpu_totalavg_system_percentage',
        ),
        migrations.RemoveField(
            model_name='devicedata',
            name='cpu_totalavg_user_percentage',
        ),
        migrations.AddField(
            model_name='devicedata',
            name='cpu_totalavg',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
