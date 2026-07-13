
from rest_framework import serializers
from .models import UserRegistration

class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = "__all__"

        #fields = ["user_id","user_name"]


