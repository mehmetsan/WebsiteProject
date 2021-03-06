# Generated by Django 3.1.3 on 2020-12-02 09:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_auto_20201202_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('Article', 'ARTICLE'), ('News', 'NEWS')], default='ARTICLE', max_length=20)),
                ('title', models.CharField(max_length=120, null=True, unique=True)),
                ('author', models.CharField(max_length=120, null=True)),
                ('body', ckeditor.fields.RichTextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_as_day', models.DateField(auto_now_add=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='news/pictures/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='news/thumbnails/')),
                ('publishable', models.BooleanField(blank=True, default=False, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=130, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('slider', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.slider')),
                ('tags', models.ManyToManyField(to='posts.Tag')),
            ],
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='slider',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='NewsPost',
        ),
    ]
