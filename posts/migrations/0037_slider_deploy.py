# Generated by Django 3.1.3 on 2021-01-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_auto_20210114_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='deploy',
            field=models.BooleanField(default=False),
        ),
    ]
