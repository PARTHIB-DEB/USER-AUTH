from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name=validated_data.pop('last_name')
        
        # Create User object with the attributes
        
        user_obj=User.objects.create_user(username=username,email=email,password=password)
        user_obj.first_name=first_name
        user_obj.last_name=last_name
        user_obj.save()
        return user_obj

    def update(self, instance, validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance




            
        

