# Generated by Django 2.2.1 on 2019-09-21 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyexpense', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='date',
            new_name='exdate',
        ),
    ]
