# Generated by Django 2.1.5 on 2021-12-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211207_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
