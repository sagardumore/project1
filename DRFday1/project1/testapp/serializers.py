from testapp.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    eid = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    sal = serializers.FloatField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.eid = validated_data.get("eid",instance.eid)
        instance.name = validated_data.get("name",instance.name)
        instance.sal = validated_data.get("sal",instance.sal)
        instance.email = validated_data.get("email",instance.email)
        instance.save()
        return instance
