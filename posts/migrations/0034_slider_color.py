# Generated by Django 3.1.3 on 2021-01-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20210114_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='color',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]