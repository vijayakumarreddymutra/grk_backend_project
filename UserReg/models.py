from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import MinValueValidator,MinLengthValidator

from .validators import name_filed_validator
# Create your models here.

class UserRegistration(models.Model):

    user_id = models.IntegerField(primary_key=True,validators=[MinValueValidator(100)])
    user_name = models.CharField(max_length=30,validators=[name_filed_validator])
    user_mobile = models.CharField(max_length=12)
    user_reg_date = models.DateField(auto_now_add=True)
    user_email = models.EmailField(unique=True)

    class Meta:
        db_table = "user_registration"
        #managed = False
    '''
    def name_field_validator(self):
        if len(self.user_name) < 3 : 
            raise ValidationError({"Username":"Name Field should accept atleast 3 characters"})
        
    def clean(self):
        self.name_field_validator()
    '''
    