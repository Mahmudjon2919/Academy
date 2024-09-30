from django.db import models
from django.contrib.auth.models import AbstractUser
#from apps.users.validators import PhoneNumberValidator


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = "admin", "Admin"
        STUDENT = "student", "Student"
        guest = "guest", "Guest"


    first_name=None
    last_name=None

    full_name=models.CharField("Full_name", max_length=255)
    role=models.CharField(max_length=16, choices=UserType.choices)
    avatar=models.ImageField(null=True, blank=True)
   # phone_number_validator=PhoneNumberValidator

   # phone_number = models.CharField(
       # "Phone number",
       # validators=[phone_number_validator],
       # max_length=255,
       # unique=True
   # )

    #is_verified = models.BooleanField(default=False)

    #USERNAME_FIELD = "phone_number"
    #REQUIRED_FIELDS = []

