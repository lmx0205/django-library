# Generated by Django 2.1.3 on 2019-04-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=15, verbose_name='学号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('gender', models.CharField(max_length=2, verbose_name='姓别')),
                ('Class', models.CharField(max_length=40, verbose_name='班级')),
                ('borrowNum', models.IntegerField(default=0, verbose_name='在借册书')),
                ('allowNum', models.IntegerField(default=0, verbose_name='可借阅次数')),
            ],
        ),
    ]