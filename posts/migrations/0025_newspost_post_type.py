# Generated by Django 3.1.3 on 2020-12-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_newspost_date_as_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='post_type',
            field=models.CharField(default='NewsPost', max_length=20),
        ),
    ]
