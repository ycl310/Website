# Generated by Django 2.2.5 on 2020-02-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitedata', '0005_changes_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacy',
            name='content',
            field=models.TextField(blank=True, default=None),
        ),
    ]