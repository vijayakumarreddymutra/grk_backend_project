from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUPRegistrationSer


#post method to create a new user registration

@api_view(["POST"])
def new_user_registration(request):
    user_ser = SignUPRegistrationSer(data = request.data)

    if user_ser.is_valid():
        user_ser.save()
        return Response({"Message":"User Registered Successfully"}, status=status.HTTP_201_CREATED)
    return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)