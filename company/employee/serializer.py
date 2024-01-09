from rest_framework import serializers
from employee.models import Company,Student

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta: 
        model = Company
        fields = "__all__"
        
        

class StudentSerializer( serializers.HyperlinkedModelSerializer):
    student_id = serializers.ReadOnlyField()
    class Meta:
        model = Student
        fields = "__all__"