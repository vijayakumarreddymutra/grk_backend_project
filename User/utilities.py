from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens(user):

    refresh = RefreshToken()

    # Add custom data to the JWT payload
    
    refresh["email"] = user.user_email  #here user is validated dict

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }
	
	
	
	