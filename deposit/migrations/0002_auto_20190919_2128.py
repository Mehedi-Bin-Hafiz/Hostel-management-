# Generated by Django 2.2.1 on 2019-09-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='date',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='name',
        ),
        migrations.AddField(
            model_name='deposit',
            name='abirdepo',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='bikidepo',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='mehedidepo',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='nurudepo',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='omardepo',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='shafindepo',
            field=models.FloatField(null=True),
        ),
    ]
