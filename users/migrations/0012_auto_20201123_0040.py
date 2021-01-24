# Generated by Django 3.1.3 on 2020-11-22 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_customuser_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('(^[A-Za-z]{3,16})([ ]{0,1})([A-Za-z]{3,16})?([ ]{0,1})?([A-Za-z]{3,16})?([ ]{0,1})?([A-Za-z]{3,16})', 'Enter a valid username. This value may contain only letters, numbers and _ character.', 'invalid')]),
        ),
    ]
