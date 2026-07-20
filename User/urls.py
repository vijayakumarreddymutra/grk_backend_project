
from django.urls import path

from .views import *

urlpatterns = [
   path("userregistration/", new_user_registration)
]
