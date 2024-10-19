from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class ProfilePage(models.Model):
    user = models.ForeignKey(
        User,
        related_name="profile_page",
        on_delete=models.CASCADE,        
    )
    
    EVACUATION_STATUS = (
        ("evacuated", "Evacuated"),
        ("non_evacuated","Non-Evacuated"),
    )
    
    evacuation_status = models.CharField(max_length=30, choices=EVACUATION_STATUS, default="non_evacuated")


    def __str__(self):
        return f"{self.user} Profile Page"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    