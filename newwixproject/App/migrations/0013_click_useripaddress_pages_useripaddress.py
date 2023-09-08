# Generated by Django 4.2.4 on 2023-08-30 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_hover_useripaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='userIPAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.webinfo'),
        ),
        migrations.AddField(
            model_name='pages',
            name='userIPAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.webinfo'),
        ),
    ]
