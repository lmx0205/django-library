# Generated by Django 2.1.3 on 2019-04-18 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0002_auto_20190418_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnform',
            name='borrowTime',
        ),
    ]