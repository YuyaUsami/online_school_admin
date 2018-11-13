# Generated by Django 2.1.2 on 2018-11-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('gender', models.CharField(blank=True, choices=[('女', '女'), ('男', '男')], max_length=2, verbose_name='性別')),
                ('age', models.IntegerField(verbose_name='年齢')),
            ],
        ),
    ]