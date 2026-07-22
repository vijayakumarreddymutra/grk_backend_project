from django.db import models

# Create your models here.


class Registration(models.Model):

    #id = models.AutoField()   - this field will generate the new value every record is created
    user_id = models.IntegerField(primary_key=True,auto_created=True)

    user_name = models.CharField(max_length=30)

    user_email = models.EmailField(unique=True)

    dob = models.DateField()

    user_reg_date = models.DateTimeField(auto_now_add=True)

    password = models.CharField(max_length=255)

    gender = models.CharField(max_length=10, default="Male")

    class Meta:
        db_table = "registration"
