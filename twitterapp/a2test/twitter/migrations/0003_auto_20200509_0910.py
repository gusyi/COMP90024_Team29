# Generated by Django 3.0.6 on 2020-05-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20200508_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='userid',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
