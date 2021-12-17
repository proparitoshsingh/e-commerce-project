# Generated by Django 4.0 on 2021-12-15 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='no address', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 14, 1, 2, 909306)),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.TextField(blank=True, default=''),
        ),
    ]