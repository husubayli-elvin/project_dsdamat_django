# Generated by Django 3.1.4 on 2020-12-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('span', models.CharField(max_length=70, verbose_name='Span')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(upload_to='blog_images', verbose_name='Resim')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]