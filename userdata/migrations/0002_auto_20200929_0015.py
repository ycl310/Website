# Generated by Django 3.0.7 on 2020-09-28 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='guild',
            unique_together=set(),
        ),
    ]