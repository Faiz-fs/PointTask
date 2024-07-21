from rest_framework import serializers
from .models import User,AppDetails,TaskDetail

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'  # Serialize all fields in the User model
  
# Serializer for the AppDetails model      
class AppDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppDetails
        fields='__all__'  # Serialize all fields in the AppDetails model

# Serializer for the TaskDetail model
class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskDetail
        fields='__all__'  # Serialize all fields in the TaskDetail model