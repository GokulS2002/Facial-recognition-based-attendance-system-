from django.db import models
 

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    s3_image_url = models.URLField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)