from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    number = serializers.IntegerField(required=False)
    
    def create(self, validated_data):
        return Student.object.create(**validated_data)   ## {firstname: 'ali', lastname:'veli' number:12345}

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ["id", "first_name", "last_name", "number"]
#         fields = '__all__'
#         exclude = ['number']