from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator

# Create your models here.
#class CustomUser(AbstractUser):
#	mobile = models.CharField(verbose_name="Phone number", max_length=10,
#    validators=[int_list_validator(sep=''),MinLengthValidator(10),], 
#    default='1234567890')