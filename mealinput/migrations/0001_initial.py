# Generated by Django 2.2.1 on 2019-09-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MealInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('mehedil', models.IntegerField(null=True)),
                ('mehedid', models.IntegerField(null=True)),
                ('omarl', models.IntegerField(null=True)),
                ('omard', models.IntegerField(null=True)),
                ('shafinl', models.IntegerField(null=True)),
                ('shafind', models.IntegerField(null=True)),
                ('bikil', models.IntegerField(null=True)),
                ('bikid', models.IntegerField(null=True)),
                ('nurul', models.IntegerField(null=True)),
                ('nurud', models.IntegerField(null=True)),
                ('abirl', models.IntegerField(null=True)),
                ('abird', models.IntegerField(null=True)),
            ],
        ),
    ]
