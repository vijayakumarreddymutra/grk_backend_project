from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserRegistration

from .serializers import UserRegSerializer
import secrets

# Create your views here.
@api_view(["GET"])
def homepage(request):
    return Response({"Message":"Welcome all!"})


@api_view(["GET"])
def homepage1(request):
    return Response({"Message":"Welcome all!"})

@api_view(["POST"])
def user_creation(request):
    print(f"method name :{request.method}")
    user_reg = UserRegSerializer(data=request.data)   #here request.data = dict format we give in postman
    
    if user_reg.is_valid():
        #print(type(user_reg.validated_data))
        user_reg.save()
        return Response({"Success Message":"User Has been Created"})
    return Response(user_reg.errors)

@api_view(["GET"])
def get_all_users_data(request):
    user_data = UserRegistration.objects.all()
    print(user_data)
    serializer = UserRegSerializer(user_data, many=True)
    print(serializer)
    return Response(serializer.data)

@api_view(["GET"])
def generate_otp(request,mobile):
    user_data = UserRegistration.objects.filter(user_mobile=mobile)

    if user_data:
        otp_pin = ''.join(secrets.choice('0123456789') for _ in range(6))
        print(otp_pin)
        return Response({"Message":otp_pin})
    return Response({"Message":"Invalid mobile num"})