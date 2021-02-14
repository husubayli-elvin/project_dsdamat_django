# Generated by Django 3.1.4 on 2021-02-10 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_customer'),
        ('order', '0003_auto_20210210_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer'),
        ),
    ]
