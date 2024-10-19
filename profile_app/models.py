from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Companion(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    RELATIONSHIP_TYPE = (
        ('select_option', 'Select Option'),
        ('spouse', 'Spouse'),
        ('parent','Parent'),
        ('child', 'Child'),
        ('sibling', 'Sibling'),
        ('in-law', 'In-Law'),
        ('friend', 'Friend'),
        ('neighbor', 'Neighbor'),
    )
    
    relationship_type = models.CharField(max_length=30, choices=RELATIONSHIP_TYPE, default='select_option')
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
    
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
    
    companion_list = models.ManyToManyField(Companion, related_name='companions')


    def __str__(self):
        return f"{self.user} Profile Page"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    