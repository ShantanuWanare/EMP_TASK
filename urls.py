from django.urls import path
from .views import EmployeeAPI, EmpAPI

urlpatterns = [
    path('emp/', EmployeeAPI.as_view()),
    path('emp/<int:pk>/', EmpAPI.as_view()),
]
