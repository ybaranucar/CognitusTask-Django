from rest_framework import serializers
from .models import Data

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Data
		fields ='__all__'
  
  
  
# class DataSerializer(serializers.Serializer):
#     label = serializers.CharField(max_length=30)
#     text = serializers.TextField()
    
#     def create (self, valideted_data):
#         return Data.objects.create(valideted_data)
    
#     def update (self, instance, valideted_data):
#         instance.label = valideted_data.get('label', instance.label)
#         instance.text = valideted_data.get('text', instance.text)
#         instance.save()
#         return instance