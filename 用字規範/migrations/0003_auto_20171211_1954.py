# Generated by Django 2.1.dev20171211115128 on 2017-12-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('用字規範', '0002_auto_20171211_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='語料庫用字',
            name='備註',
            field=models.TextField(blank=True),
        ),
    ]
