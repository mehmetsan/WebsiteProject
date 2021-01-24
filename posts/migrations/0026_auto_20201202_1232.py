# Generated by Django 3.1.3 on 2020-12-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_newspost_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='post_type',
            field=models.CharField(choices=[('ARTICLE', 'Article'), ('NEWS', 'NewsPost')], default='ARTICLE', max_length=20),
        ),
    ]
