# Generated by Django 3.1.3 on 2020-11-23 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20201123_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='slider_picture',
            new_name='picture',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='news_post',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider_body',
        ),
        migrations.AddField(
            model_name='article',
            name='slider',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
