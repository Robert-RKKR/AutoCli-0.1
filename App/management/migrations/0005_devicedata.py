# Generated by Django 3.2.7 on 2021-10-30 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20211030_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hostname', models.CharField(blank=True, max_length=64, null=True)),
                ('system_version', models.CharField(blank=True, max_length=64, null=True)),
                ('domain_name', models.CharField(blank=True, max_length=50, null=True)),
                ('default_gateway', models.GenericIPAddressField(blank=True, null=True)),
                ('name_server_list', models.JSONField(blank=True, null=True)),
                ('ntp_server_list', models.JSONField(blank=True, null=True)),
                ('os_boot_files_list', models.JSONField(blank=True, null=True)),
                ('ios_users_list', models.JSONField(blank=True, null=True)),
                ('snmp_server_community_list', models.JSONField(blank=True, null=True)),
                ('snmp_server_group_list', models.JSONField(blank=True, null=True)),
                ('snmp_server_user_list', models.JSONField(blank=True, null=True)),
                ('spanning_tree_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.device')),
            ],
        ),
    ]