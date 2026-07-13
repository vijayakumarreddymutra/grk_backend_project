
import requests

data = {
    "user_id": 108,
    "user_name": "Virat",
    "user_mobile" : 0,
    "user_email" : "vk8@vk.in" 

}

#res = requests.get("http://127.0.0.1:8000/api/allusers/")
res = requests.post("http://127.0.0.1:8000/api/usercreate/", data=data)

print(res.json())
print(res.status_code)