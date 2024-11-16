from django.shortcuts import render
from rest_framework import viewsets
# from api.models import *
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

# for custom api
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        print("get employees of",pk,"company")
        pass

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
