# Generated by Django 4.1.13 on 2024-04-15 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_userprofile_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'managed': False},
        ),
    ]
