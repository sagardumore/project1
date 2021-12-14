from django.shortcuts import render

from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def employee_details(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def employee_info(request,id):
    if request.method == 'GET':
        if id :
            try:
                emp = Employee.objects.get(id=id)
            except Employee.DoesNotExist:
                return Response({'msg':'record doest not exist'})
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        return Response({'msg':'plzz provide the id'})

    elif request.method == 'PUT':
        if id :
            try:
                emp = Employee.objects.get(id=id)
            except Employee.DoesNotExist:
                return Response({'msg':'record doest not exist'})
            serializer = EmployeeSerializer(emp, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'msg':'plzz send valid data'})
        return Response({'msg':'plzz send id'})

    elif request.method == 'DELETE':
        if id :
            try:
                emp = Employee.objects.get(id=id)
            except Employee.DoesNotExist:
                return Response({'msg':'record doest not exist'})
            emp.delete()
            return Response({'msg':'Record deleted successfully'})
        return Response({'msg':'plzz send id'})