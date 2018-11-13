from django.urls import path
from .import views

app_name = 'customer'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('record', views.RecordListView.as_view(), name='record'),
    path('record/add', views.RecordCreateView.as_view(), name='recordadd'),
    path('record/update/<int:pk>', views.RecordUpdateView.as_view(), name='recordupdate'),
    path('billing', views.BillingListView.as_view(), name='billing'),
]