# Generated by Django 4.1.13 on 2024-05-06 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_userprofile_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='userprofiles',
        ),
    ]