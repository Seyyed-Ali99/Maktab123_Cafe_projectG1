# Generated by Django 5.1.6 on 2025-03-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customers_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer')], default='customer', max_length=10),
        ),
    ]
