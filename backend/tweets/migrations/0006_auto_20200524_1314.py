# Generated by Django 3.0.6 on 2020-05-24 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20200521_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='migration_number',
            field=models.IntegerField(blank=True, default=0, help_text='Integer', null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='migration_percentage',
            field=models.DecimalField(decimal_places=3, help_text='decimal, 0-1', max_digits=6),
        ),
        migrations.AlterField(
            model_name='tweetresultdata',
            name='cityname',
            field=models.CharField(choices=[('Melbourne', 'Melbourne'), ('Geelong', 'Geelong'), ('Ballarat', 'Ballarat'), ('Bendigo', 'Bendigo'), ('Victoria', 'Victoria'), ('Melton', 'Melton')], default='Melbourne', max_length=30),
        ),
    ]
