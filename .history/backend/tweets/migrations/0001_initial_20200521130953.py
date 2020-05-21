# Generated by Django 3.0.6 on 2020-05-21 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Melbourne', max_length=30)),
                ('average_income', models.IntegerField()),
                ('education_level', models.CharField(blank=True, max_length=50)),
                ('migration_percentage', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='TweetResultData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('tweetcounts', models.IntegerField()),
                ('approval_rate', models.DecimalField(decimal_places=5, max_digits=6)),
                ('cityname', models.CharField(choices=[('Melbourne', 'Melbourne'), ('Geelong', 'Geelong'), ('Ballarat', 'Ballarat'), ('Bendigo', 'Bendigo'), ('Melton', 'Melton')], default='Melbourne', max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.City')),
            ],
        ),
    ]
