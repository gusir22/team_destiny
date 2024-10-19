from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    street_address = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    zip_code = models.TextField(max_length=5)
    
    phone_number = models.CharField(
        max_length=12,
        help_text="Please use the xxx-xxx-xxxx format.",
        validators=[
            RegexValidator(r"\d{3}-\d{3}-\d{4}", "Please enter a valid phone number in the xxx-xxx-xxxx format.")
        ],
    )
    
    profile_photo = models.ImageField(upload_to='profile_photos/')
    
    
    
    def formal_address(self):
        return f"{self.street_address}, {self.city}, Florida {self.zip_code}"
    
    def __str__(self) -> str:
        return self.get_full_name()