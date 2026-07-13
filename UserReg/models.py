from django.db import models


from django.core.validators import MinValueValidator,MinLengthValidator
# Create your models here.

class UserRegistration(models.Model):

    user_id = models.IntegerField(primary_key=True,validators=[MinValueValidator(100)])
    user_name = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    user_mobile = models.IntegerField()
    user_reg_date = models.DateField(auto_now_add=True)
    user_email = models.EmailField(unique=True)

    class Meta:
        db_table = "user_registration"
        #managed = False

     
        