from rest_framework import serializers
from api.models import Company,Employee

# creating serializers here

# serializers.HyperlinkedModelSerializer is a child class
# we are making meta class here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:  
        model = Company
        fields = "__all__"
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"
class employeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"
