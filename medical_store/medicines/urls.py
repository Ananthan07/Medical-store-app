# medical_store_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('add/', views.add_medicine, name='add_medicine'),
    path('edit/<int:medicine_id>/', views.edit_medicine, name='edit_medicine'),
    path('delete/<int:id>/', views.delete_medicine, name='delete_medicine'),
    path('list/', views.list_medicines, name='list_medicines'),
    path('search/', views.search_medicine, name='search_medicine'),
]
