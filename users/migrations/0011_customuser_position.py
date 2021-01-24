# Generated by Django 3.1.3 on 2020-11-22 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201122_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^\\w+$', 'Enter a valid username. This value may contain only letters, numbers and _ character.', 'invalid')]),
        ),
    ]