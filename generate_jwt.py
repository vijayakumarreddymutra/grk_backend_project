from rest_framework_simplejwt.tokens import RefreshToken

refresh = RefreshToken()  #here it is creating object and that object is dict

# Add custom data to the JWT payload
refresh["user_id"] = "vj_kumarreddy"
refresh["email"] = "vj123@vj.in"

token = {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }
	
print(token)