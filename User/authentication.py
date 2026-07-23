

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken

from .models import Registration

class RegistrationJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        auth = request.headers.get("Authorization")   #here auth is returning sting value like "Bearer eykhkdjfhjk..."
        print(f"YOur auth is {auth}")

        if not auth:
            return None

        try:
            token = auth.split(" ")[1]

            payload = AccessToken(token)

            user = Registration.objects.get(
                user_email=payload["email"]
            )

            return (user, None)

        except Exception as e:
            import traceback
            traceback.print_exc()
            raise AuthenticationFailed(str(e))
			