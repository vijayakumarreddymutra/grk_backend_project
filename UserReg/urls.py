
from django.urls import path

from.views import *

urlpatterns = [
    path("message/",homepage),
    path("hello/",homepage1),
    path("usercreate/",user_creation),
    path("singleuser/",filter_user_Data_using_query),
    path("allusers/",get_all_users_data),
    path("generateotp/<int:mobile>",generate_otp),
    path("userpartialupdate/<int:id>",update_user_partial_data),
    path("userupdate/<int:id>",update_user_data),
    path("userdelete/<int:id>",user_delete),
    path("allusersdelete/",all_users_delete)
]
