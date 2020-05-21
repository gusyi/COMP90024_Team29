# Generated by Django 3.0.6 on 2020-05-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tweetresultdata',
            options={'ordering': ['date', 'city']},
        ),
        migrations.AddField(
            model_name='city',
            name='migration_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tweetresultdata',
            name='approval_rate',
            field=models.DecimalField(decimal_places=5, help_text='decimal, 0-1', max_digits=6),
        ),
    ]