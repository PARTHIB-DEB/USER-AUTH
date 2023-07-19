from rest_framework import serializers
from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data): # For nee object creation / POST request only
        
        # Filling details in each parameter of User model from 'validated_data' list
        
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name=validated_data.pop('last_name')
        
        #Writing validations and creating Object of 'User' model
        
        if User.objects.filter(email=email).count()==0: #Checking the email
               
            if User.objects.filter(password=password).count()==0: # Checking the password
                   
                if len(password)>=8: # Verfications for every new password
                    user_obj=User.objects.create_user(username=username,email=email,password=password)
                    user_obj.first_name=first_name
                    user_obj.last_name=last_name
                    user_obj.save()
                    return user_obj
                else:
                    raise serializers.ValidationError('PASSWORD TOO SHORT')
            else:
                raise serializers.ValidationError('PASSWORD ENTERED BY SOMEONE BEFORE')
        else:
            raise serializers.ValidationError('EMAIL ENTERED BY SOMEONE BEFORE')

    def update(self, instance, validated_data): # For updation of an existing 'User' object
        # updating every/ specific fields (mentioned here only) 
        instance.username=validated_data.get('username',instance.username) 
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance




            
        

