# Generated by Django 3.1.3 on 2020-11-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20201127_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='make_slider',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]