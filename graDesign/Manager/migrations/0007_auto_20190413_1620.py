# Generated by Django 2.1.3 on 2019-04-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0006_auto_20190407_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='name',
            field=models.CharField(default=1, max_length=20, verbose_name='管理员名字'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='managers',
            name='manager',
            field=models.CharField(max_length=20, verbose_name='管理员类型'),
        ),
    ]
