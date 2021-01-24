# Generated by Django 3.1.3 on 2020-11-20 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'A user with that email already exists.'}, max_length=254, null=True, unique=True, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, help_text='Enter phone number with our without +()', max_length=30, null=True, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', 'Enter a valid phone number.', 'invalid')], verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'The username is already taken.'}, max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^\\w+$', 'Enter a valid username. This value may contain only letters, numbers and _ character.', 'invalid')]),
        ),
    ]
