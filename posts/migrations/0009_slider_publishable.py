# Generated by Django 3.1.3 on 2020-11-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20201123_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='publishable',
            field=models.BooleanField(default=False),
        ),
    ]
