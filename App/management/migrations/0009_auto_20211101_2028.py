# Generated by Django 3.2.7 on 2021-11-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20211031_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicedata',
            name='cpu_totalavg_idle_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='cpu_totalavg_system_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='cpu_totalavg_user_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='images_files_list',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='memory_available_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='memory_status',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='memory_total_mb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='memory_used_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='partitions_list',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
