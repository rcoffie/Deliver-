# Generated by Django 3.2.9 on 2022-01-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_ordermodel_order_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='menu_images/'),
        ),
    ]
