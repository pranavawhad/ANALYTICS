# Generated by Django 4.2.4 on 2023-08-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='typeC',
            field=models.CharField(blank=True, max_length=123124214, null=True),
        ),
        migrations.AddField(
            model_name='hover',
            name='type',
            field=models.CharField(blank=True, max_length=121212, null=True),
        ),
    ]