from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomerCreateForm
from .models import Customer


# class IndexView(generic.TemplateView):
#   template_name = 'customer/customer_list.html'

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