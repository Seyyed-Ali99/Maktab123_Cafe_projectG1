# Generated by Django 5.0.8 on 2025-02-24 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='ordersdetails',
            options={'verbose_name_plural': 'OrderDetails'},
        ),
        migrations.AlterModelOptions(
            name='reciepts',
            options={'verbose_name_plural': 'Reciepts'},
        ),
        migrations.AlterModelOptions(
            name='tables',
            options={'verbose_name_plural': 'Tables'},
        ),
    ]
