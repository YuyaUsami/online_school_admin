from django import forms
from .models import Customer, Lesson, LessonRecord, ChangeFee


class CustomerCreateForm(forms.ModelForm):

  class Meta:
    model = Customer
    fields = '__all__'

class RecordUpdateView(forms.ModelForm):

  class Meta:
    model = LessonRecord
    fields = ("lesson_date", "attending_time", "lesson", "customer")

class RecordCreateView(forms.ModelForm):

  class Meta:
    model = LessonRecord
    fields = ("lesson_date", "attending_time", "lesson", "customer")