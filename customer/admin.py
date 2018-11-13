from django.contrib import admin
from .models import Customer, Lesson, LessonRecord, ChangeFee

admin.site.register(Customer)
admin.site.register(Lesson)
admin.site.register(LessonRecord)
admin.site.register(ChangeFee)