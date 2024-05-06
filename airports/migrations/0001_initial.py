# Generated by Django 4.1.13 on 2024-04-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('airportX', models.FloatField()),
                ('airportY', models.FloatField()),
                ('airport_age', models.IntegerField()),
                ('flights_inbound', models.IntegerField()),
                ('flights_outbound', models.IntegerField()),
                ('delays_at_arrival', models.IntegerField()),
                ('delays_at_departure', models.IntegerField()),
                ('busyness', models.CharField(max_length=20)),
                ('airplane_capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'Airports',
                'managed': False,
            },
        ),
    ]
