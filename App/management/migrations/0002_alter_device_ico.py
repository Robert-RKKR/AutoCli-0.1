# Generated by Django 3.2.7 on 2021-10-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='ico',
            field=models.IntegerField(choices=[(1, 'static/management/svg/metro-1500.svg')], default=1),
        ),
    ]
