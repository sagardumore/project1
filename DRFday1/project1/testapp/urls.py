from django.urls import path
from testapp.views import employee_details, employee_info

urlpatterns = [
    path('details/',employee_details),
    path('details/<int:id>/',employee_info)
]