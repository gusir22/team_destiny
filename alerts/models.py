from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db import models



User = get_user_model()

# Create your models here.
class Alert(TimeStampedModel):
    title = models.TextField(max_length=150)
    description = models.TextField()
    STATUS = (
        ("active", "Active"),
        ("resolved", "Resolved"),
    )
    status = models.CharField(max_length=10, choices=STATUS, default="active")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"
    