# Generated by Django 2.1.5 on 2019-01-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(max_length=10)),
                ('wind_speed', models.IntegerField()),
                ('high_temp', models.IntegerField()),
                ('min_temp', models.IntegerField()),
                ('rain', models.IntegerField()),
            ],
        ),
    ]
