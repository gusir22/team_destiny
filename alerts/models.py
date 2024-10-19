from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db import models



User = get_user_model()

class ZipCode(models.Model):
    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.code
    

# Create your models here.
class Alert(TimeStampedModel):
    title = models.TextField(max_length=150)
    description = models.TextField()
    STATUS = (
        ("active", "Active"),
        ("resolved", "Resolved"),
    )
    status = models.CharField(max_length=10, choices=STATUS, default="active")
    
    affected_zip_code = models.ManyToManyField(ZipCode, related_name="alert_zip_codes")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = [
            '-modified',
            '-created',
            ]
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"
  
  
class AlertUpdate(TimeStampedModel):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name="alert_updates")
    description = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = [
            '-modified',
            '-created',
            ]
    
    def __str__(self):
        return f"{self.alert.title} - Update {self.id}"
    