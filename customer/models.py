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