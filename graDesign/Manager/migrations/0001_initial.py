# Generated by Django 2.1.3 on 2019-04-01 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, verbose_name='图书编号')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='书名')),
                ('author', models.CharField(max_length=10, null=True, verbose_name='作者')),
                ('style', models.CharField(max_length=15, verbose_name='类型')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('press', models.CharField(max_length=40, verbose_name='出版社')),
                ('place', models.CharField(max_length=5, verbose_name='存放位置')),
                ('borrowedNum', models.IntegerField(default=0, verbose_name='被借次数')),
            ],
        ),
        migrations.CreateModel(
            name='borrowForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowTime', models.DateTimeField(auto_now_add=True, verbose_name='借书时间')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Manager.books', verbose_name='图书')),
            ],
        ),
        migrations.CreateModel(
            name='returnForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowTime', models.DateTimeField(auto_now_add=True, verbose_name='借书时间')),
                ('returnTime', models.DateTimeField(auto_now_add=True, verbose_name='还书时间')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Manager.books', verbose_name='图书')),
            ],
        ),
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
        migrations.AddField(
            model_name='returnform',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Manager.students', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='borrowform',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Manager.students', verbose_name='学生'),
        ),
    ]