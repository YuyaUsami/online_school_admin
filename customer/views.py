from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomerCreateForm, RecordCreateView, RecordUpdateView
from .models import Customer, Lesson, LessonRecord, ChangeFee

class IndexView(generic.ListView):
  model = Customer

class AddView(LoginRequiredMixin, generic.CreateView):
  model = Customer
  form_class = CustomerCreateForm
  success_url = reverse_lazy('customer:index')

class UpdateView(LoginRequiredMixin, generic.UpdateView):
  model = Customer
  form_class = CustomerCreateForm
  success_url = reverse_lazy('customer:index')

class RecordListView(ListView):
  model = LessonRecord
  template_name = 'customer/record_list.html'

class RecordUpdateView(UpdateView):
  model = LessonRecord
  form_class = LessonRecord

class RecordCreateView(CreateView):
  model = LessonRecord
  form_class = LessonRecord

class BillingListView(generic.TemplateView):
  template_name = 'customer/billing_list.html'
