# Generated by Django 3.0.7 on 2020-09-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200929_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
