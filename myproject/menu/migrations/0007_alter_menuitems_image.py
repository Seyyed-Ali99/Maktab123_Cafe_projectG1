# Generated by Django 5.1.6 on 2025-02-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_menuitems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu/images/'),
        ),
    ]
