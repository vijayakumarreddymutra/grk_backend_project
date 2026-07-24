

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUPRegistrationSer, LoginSerializer
from .utilities import get_tokens

import logging

logs = logging.getLogger(__name__)

#post method to create a new user registration

@api_view(["POST"])
def new_user_registration(request):
    user_ser = SignUPRegistrationSer(data = request.data)

    if user_ser.is_valid():
        user_ser.save()
        return Response({"Message":"User Registered Successfully"}, status=status.HTTP_201_CREATED)
    return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])  #if we want to pass the data, we have to use POST method only
def login(request):
    logs.debug("User Tried to login")
    user_data = LoginSerializer(data=request.data)

    if user_data.is_valid():
        user = user_data.validated_data["user"]   #here validated_data is equal to attrs in serializer
        tokens = get_tokens(user)
        logs.info("User loggined in successfully and generated the tokens")
        return Response({"message":"Login Successfull",
                         "access_token": tokens["access"],
                        "refresh_token": tokens["refresh"]},
                        status=status.HTTP_200_OK)

    logs.warning("Unauthorized user tried to access")
    return Response(user_data.errors,status=status.HTTP_401_UNAUTHORIZED)
    