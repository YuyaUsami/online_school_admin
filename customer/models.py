from django.db import models
from django.utils import timezone

GENDER_CHOICES = (
    ("男", '男'),
    ("女", '女'),
)

class Customer(models.Model):
  name = models.CharField('名前', max_length=20)
  gender = models.CharField('性別', max_length=2, blank=True, choices=GENDER_CHOICES)
  age = models.IntegerField('年齢')

  def __str__(self):
    return self.name

class Lesson(models.Model):
  basic_fee = models.IntegerField('基本料金')
  category = models.CharField('ジャンル', max_length=50)

  def __str__(self):
    return self.category

class LessonRecord(models.Model):
  lesson_date = models.DateField('受講日')
  lesson = models.ForeignKey(
    Lesson, verbose_name='授業', on_delete=models.PROTECT,
  )
  customer = models.ForeignKey(
    Customer, verbose_name='顧客', on_delete=models.PROTECT,
  )
  def __str__(self):
    return self.lesson_date

class ChangeFee(models.Model):
  boundary_time = models.IntegerField('境界時間')
  per_user_fee = models.IntegerField('従量料金')
  lesson = models.ForeignKey(
    Lesson, verbose_name='授業', on_delete=models.PROTECT,
  )