from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_page'),
    path('employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('employees/add/', views.employee_create, name='add_employee'),
    path('employees/<int:id>/edit/', views.employee_edit, name='employee_edit'), 
    path('employees/<int:id>/delete/', views.employee_delete, name='employee_delete'),
    path('search/', views.search_employee.as_view(), name='search_employee'),
]