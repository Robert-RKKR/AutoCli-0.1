# Generated by Django 3.2.7 on 2021-11-11 12:56

from django.db import migrations, models
import django.db.models.deletion
import management.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('username', models.CharField(max_length=64)),
                ('description', models.CharField(default='Device credential description', max_length=512)),
                ('password', models.CharField(max_length=64, null=True)),
                ('secret', models.CharField(blank=True, max_length=64, null=True)),
                ('token', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Nonactive'), (1, 'Active'), (2, 'ToBin')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ssh_status', models.BooleanField(default=False)),
                ('https_status', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('hostname', models.CharField(error_messages={'blank': 'This field is mandatory.', 'null': 'This field is mandatory.', 'unique': 'This field must be unique.'}, help_text='Enter a valid IP address or hostname.', max_length=64, unique=True)),
                ('device_type', models.IntegerField(choices=[(0, 'autodetect'), (1, 'cisco_ios'), (2, 'cisco_xr'), (3, 'cisco_xe'), (4, 'cisco_nxos')], default=0)),
                ('ico', models.IntegerField(choices=[(0, 'static/management/svg/router.svg'), (1, 'static/management/svg/asa-5500.svg'), (2, 'static/management/svg/atm-router.svg'), (3, 'static/management/svg/cisco-asa-5500.svg'), (4, 'static/management/svg/director-class-fibre-channel-di.svg'), (5, 'static/management/svg/firewall-service-module-fwsm.svg'), (6, 'static/management/svg/firewall.svg'), (7, 'static/management/svg/generic-gateway.svg'), (8, 'static/management/svg/ios-firewall.svg'), (9, 'static/management/svg/layer-3-switch.svg'), (10, 'static/management/svg/nexus-2000-fabric-extender.svg'), (11, 'static/management/svg/nexus-5000.svg'), (12, 'static/management/svg/nexus-7000.svg'), (13, 'static/management/svg/route-switch-processor.svg'), (14, 'static/management/svg/router-firewall.svg'), (15, 'static/management/svg/accesspoint.svg'), (16, 'static/management/svg/wireless-router.svg'), (17, 'static/management/svg/workgroup-switch.svg'), (18, 'static/management/svg/cloud.svg'), (19, 'static/management/svg/fibre-channel-fabric-switch.svg'), (20, 'static/management/svg/ground-terminal.svg'), (21, 'static/management/svg/mesh-ap.svg'), (22, 'static/management/svg/modem.svg'), (23, 'static/management/svg/netflow-router.svg'), (24, 'static/management/svg/telecommuter-house.svg'), (25, 'static/management/svg/vpn-gateway.svg'), (26, 'static/management/svg/wavelength-router.svg')], default=0)),
                ('ssh_port', models.IntegerField(default=22)),
                ('https_port', models.IntegerField(default=443)),
                ('description', models.CharField(default='Device description', max_length=512)),
                ('secret', models.CharField(blank=True, max_length=64, null=True)),
                ('token', models.CharField(blank=True, max_length=128, null=True)),
                ('certificate', models.BooleanField(default=False)),
                ('credential', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='management.credential')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('color', models.CharField(blank=True, error_messages={'blank': 'This field is mandatory.', 'invalid': 'Enter the correct colour value. It must be a 3/6 character hexadecimal number with # on begining', 'null': 'This field is mandatory.'}, help_text='Hexadecimal representation of colour, for example #73a6ff.', max_length=8, null=True, validators=[management.validators.ColorValidator()])),
                ('description', models.CharField(default='Color description', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='TestDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('hostname', models.CharField(error_messages={'blank': 'This field is mandatory.', 'null': 'This field is mandatory.', 'unique': 'This field must be unique.'}, help_text='Enter a valid IP address or hostname.', max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestHttpsDevice',
            fields=[
                ('testdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.testdevice')),
                ('https_status', models.BooleanField(default=False)),
                ('https_port', models.IntegerField(default=443)),
            ],
            bases=('management.testdevice',),
        ),
        migrations.CreateModel(
            name='TestSshDevice',
            fields=[
                ('testdevice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.testdevice')),
                ('device_type', models.IntegerField(choices=[(0, 'autodetect'), (1, 'cisco_ios'), (2, 'cisco_xr'), (3, 'cisco_xe'), (4, 'cisco_nxos')], default=0)),
                ('ssh_status', models.BooleanField(default=False)),
                ('ssh_port', models.IntegerField(default=22)),
            ],
            bases=('management.testdevice',),
        ),
        migrations.CreateModel(
            name='TagDeviceRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.device')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.tag')),
            ],
            options={
                'unique_together': {('device', 'tag')},
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='devices',
            field=models.ManyToManyField(through='management.TagDeviceRelation', to='management.Device'),
        ),
        migrations.CreateModel(
            name='SshDeviceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('version', models.CharField(blank=True, max_length=64, null=True)),
                ('rommon', models.CharField(blank=True, max_length=64, null=True)),
                ('hostname', models.CharField(blank=True, max_length=64, null=True)),
                ('uptime', models.CharField(blank=True, max_length=64, null=True)),
                ('reload_reason', models.CharField(blank=True, max_length=64, null=True)),
                ('running_image', models.CharField(blank=True, max_length=64, null=True)),
                ('config_register', models.CharField(blank=True, max_length=64, null=True)),
                ('hardware_list', models.JSONField(blank=True, null=True)),
                ('serial_list', models.JSONField(blank=True, null=True)),
                ('mac_list', models.JSONField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hostname', models.CharField(blank=True, max_length=64, null=True)),
                ('system_version', models.CharField(blank=True, max_length=64, null=True)),
                ('domain_name', models.CharField(blank=True, max_length=64, null=True)),
                ('default_gateway', models.GenericIPAddressField(blank=True, null=True)),
                ('name_server_list', models.JSONField(blank=True, null=True)),
                ('ntp_server_list', models.JSONField(blank=True, null=True)),
                ('os_boot_files_list', models.JSONField(blank=True, null=True)),
                ('ios_users_list', models.JSONField(blank=True, null=True)),
                ('snmp_server_community_list', models.JSONField(blank=True, null=True)),
                ('snmp_server_group_list', models.JSONField(blank=True, null=True)),
                ('snmp_server_user_list', models.JSONField(blank=True, null=True)),
                ('spanning_tree_mode', models.CharField(blank=True, max_length=64, null=True)),
                ('memory_stats', models.JSONField(blank=True, null=True)),
                ('cpu_stats', models.JSONField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.device')),
            ],
        ),
    ]
