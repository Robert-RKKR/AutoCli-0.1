# Generated by Django 3.2.7 on 2021-10-07 20:50

from django.db import migrations, models
import management.validators


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(error_messages={'blank': 'This field is mandatory.', 'invalid': 'Enter the correct colour value. It must be a 3/6 character hexadecimal number with # on begining', 'null': 'This field is mandatory.'}, help_text='Hexadecimal representation of colour, for example #73a6ff.', max_length=64, validators=[management.validators.ColorValidator]),
        ),
    ]
