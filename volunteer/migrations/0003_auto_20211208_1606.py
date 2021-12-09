# Generated by Django 3.2.9 on 2021-12-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_auto_20211206_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteers',
            name='password',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteers',
            name='username',
            field=models.CharField(default=2, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]