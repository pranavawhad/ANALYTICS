# Generated by Django 4.2.4 on 2023-08-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_remove_webinfo_domainname_webinfo_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinfo',
            name='Website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
