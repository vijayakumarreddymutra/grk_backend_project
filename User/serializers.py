from rest_framework import serializers
from .models import Registration
#from rest_framework.exceptions import ValidationError

from django.contrib.auth.hashers import make_password

from .validators import *

class SignUPRegistrationSer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only = True)

    user_name = serializers.CharField(validators=[validate_username])

    user_email = serializers.CharField(validators = [validate_email])

    password = serializers.CharField(validators = [validate_password])

    class Meta:
        model = Registration
        fields = "__all__"
    
    #the below will execute at the time of is_valid()method called out
    def validate(self,attrs):   #here attrs are dict formata, all model values will be saved as dict here
        if attrs["password"] != attrs["confirm_password"]:
                raise serializers.ValidationError({"message":"Passwords are not matching"})
        return attrs
    
    #when you call save() method this method will execute autoamtically
    def create(self, validated_data):
         validated_data.pop("confirm_password")

         validated_data["password"] = make_password(validated_data["password"])

         return Registration.objects.create(**validated_data)