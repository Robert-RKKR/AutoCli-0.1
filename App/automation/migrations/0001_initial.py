# Generated by Django 3.2.7 on 2021-11-06 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomationPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.CharField(default='Automation policy description', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.CharField(default='Scheduler description', max_length=512)),
                ('execute_time', models.TimeField(unique=True)),
                ('execute_date', models.DateTimeField(unique=True)),
                ('seconds', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.CharField(default='Template description', max_length=512)),
                ('value', models.TextField()),
                ('variables', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('input_data', models.TextField(null=True)),
                ('output_data', models.TextField(null=True)),
                ('automation_policy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='automation.automationpolicy')),
            ],
        ),
        migrations.AddField(
            model_name='automationpolicy',
            name='scheduler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='automation.scheduler'),
        ),
        migrations.CreateModel(
            name='TemplateAutomationPolicyRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField(unique=True)),
                ('automation_policy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='automation.automationpolicy')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='automation.template')),
            ],
            options={
                'unique_together': {('template', 'automation_policy')},
            },
        ),
        migrations.CreateModel(
            name='DeviceAutomationPolicyRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField(unique=True)),
                ('automation_policy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='automation.automationpolicy')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.device')),
            ],
            options={
                'unique_together': {('device', 'automation_policy')},
            },
        ),
    ]
