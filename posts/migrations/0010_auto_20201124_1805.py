# Generated by Django 3.1.3 on 2020-11-24 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_slider_publishable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slider',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.slider'),
        ),
    ]
