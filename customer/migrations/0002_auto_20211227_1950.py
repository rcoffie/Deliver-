# Generated by Django 3.2.9 on 2021-12-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='location',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
