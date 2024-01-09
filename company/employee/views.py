from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from employee.models import Company,Student
# Create your views here.
from employee.serializer import CompanySerializer,StudentSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    
    
    
class StudentViewSet( viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer