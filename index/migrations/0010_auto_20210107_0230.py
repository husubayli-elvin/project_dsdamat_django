# Generated by Django 3.1.4 on 2021-01-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20210107_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]