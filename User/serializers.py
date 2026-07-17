from rest_framework import serializers
from .models import Registration
from rest_framework.exceptions import ValidationError

from .validators import *

class SignUPRegistrationSer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only = True)

    user_name = serializers.CharField(validators=[validate_username])

    user_email = serializers.CharField(validators = [validate_username])

    password = serializers.CharField(validators = [validate_password])

    class Meta:
        model = Registration
        fields = "__all_"
    
    def validate(self,attrs):   #here attrs are dict formata, all model values will be saved as dict here
        if attrs["pasword"] != attrs["confirm_password"]:
                raise ValidationError({"message":"Passwords are not matching"})