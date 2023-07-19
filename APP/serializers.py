from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.mail import send_mail
from AUTH import  settings

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
        
        # Writing custom validations and creating Object of 'User' model
        
        try:
            if User.objects.filter(email=email).count()==0: #Checking the email
               
                if User.objects.filter(password=password).count()==0: # Checking the password
                   
                    if len(password)>=8: # Verfications for every new password
                        user_obj=User.objects.create_user(username=username,email=email,password=password)
                        user_obj.first_name=first_name
                        user_obj.last_name=last_name
                        user_obj.save()
                        try:
                            subject = "ACCCOUNT VERIFICATION"
                            content = "If you find this mail then your account is verified,No click on http://127.0.0.1:8000/lin/"
                            sender_email=settings.EMAIL_HOST_USER
                            receiver_email=email
                            send_mail(subject, content, sender_email, recipient_list=receiver_email, fail_silently=True)
                        except Exception as e:
                            raise serializers.ValidationError('EMAIL NOT SENT')
                        return user_obj
                    else:
                        raise serializers.ValidationError('PASSWORD TOO SHORT')
                else:
                    raise serializers.ValidationError('PASSWORD ENTERED BY SOMEONE BEFORE')
            else:
                raise serializers.ValidationError('EMAIL ENTERED BY SOMEONE BEFORE')
        except Exception as e:
            raise serializers.ValidationError(e)

    def update(self, instance, validated_data): # For updation of an existing 'User' object
        
        # updating every/ specific fields (mentioned here only) with custom validations 
        username=validated_data.get('username',instance.username)           
        if User.objects.filter(username=username).count()==0 :
            
            email=validated_data.get('email', instance.email)
            if User.objects.filter(email=email).count()==0: #Checking the email
               
                password=instance.password = validated_data.get('password', instance.password)
                if User.objects.filter(password=password).count()==0: # Checking the password
                   
                    if len(password)>=8: # Verfications for every new password
                        instance.username=validated_data.get('username',instance.username) 
                        instance.email = validated_data.get('email', instance.email)
                        instance.password = validated_data.get('password', instance.password)
                        instance.first_name = validated_data.get('first_name', instance.first_name)
                        instance.last_name = validated_data.get('last_name', instance.last_name)
                        instance.save()
                        return instance
                    else:
                        raise serializers.ValidationError('PASSWORD TOO SHORT')
                else:
                    raise serializers.ValidationError('PASSWORD ENTERED BY SOMEONE BEFORE')
            else:
                raise serializers.ValidationError('EMAIL ENTERED BY SOMEONE BEFORE')
        else:
            raise serializers.ValidationError('USERNAME ENTERED BY SOMEONE BEFORE')




            
        

