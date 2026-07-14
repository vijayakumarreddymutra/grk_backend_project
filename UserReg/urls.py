
from django.urls import path

from.views import homepage,homepage1, user_creation,get_all_users_data, generate_otp, update_user_partial_data

urlpatterns = [
    path("message/",homepage),
    path("hello/",homepage1),
    path("usercreate/",user_creation),
    path("allusers/",get_all_users_data),
    path("generateotp/<int:mobile>",generate_otp),
    path("userupdate/<int:id>",update_user_partial_data)
]
