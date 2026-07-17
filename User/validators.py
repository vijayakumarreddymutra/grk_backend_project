from rest_framework.exceptions import ValidationError

import re

def validate_username(value):
    if len(value) > 3:
        raise ValidationError("Username should contain 3 characters")
    
    if not value.isalpha():
        raise ValidationError("Username should contain only alphabets")
    
    return value

    def validate_email(value):
        if Registration.objects.get(user_email = value).exists():
            raise ValidationError("User email is already exists")
        return value
    
    def validate_password(value):

        if len(value) < 16:
            raise ValidationError("Password should contain atleast 16 characters")
        
        if not re.search(r"[A-Z]",value):
            raise ValidationError("Password should contain one Upper Case letter")
        
        if not re.search(r"[a-z]",value):
            raise ValidationError("Password should contain one lower Case letter")
        
        if not re.search(r"\d",value):
            raise ValidationError("Password should contain atleast one number")
        
        #r"[!@#$%*()]"
        return value
        
