from django.db import models
from django.contrib.auth.models import User

class WaterFaultReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    # Link to user - this connects each report to a registered user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='reports')
    
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=300)
    fault_type = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_feedback = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"