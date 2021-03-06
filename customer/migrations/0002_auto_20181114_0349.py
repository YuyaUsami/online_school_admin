# Generated by Django 2.1.2 on 2018-11-13 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boundary_time', models.IntegerField(verbose_name='境界時間')),
                ('per_user_fee', models.IntegerField(verbose_name='従量料金')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_fee', models.IntegerField(verbose_name='基本料金')),
                ('category', models.CharField(max_length=50, verbose_name='ジャンル')),
            ],
        ),
        migrations.CreateModel(
            name='LessonRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_date', models.DateTimeField(verbose_name='受講日')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('男', '男'), ('女', '女')], max_length=2, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='lessonrecord',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Customer', verbose_name='顧客'),
        ),
        migrations.AddField(
            model_name='lessonrecord',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Lesson', verbose_name='授業'),
        ),
        migrations.AddField(
            model_name='changefee',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Lesson', verbose_name='授業'),
        ),
    ]
