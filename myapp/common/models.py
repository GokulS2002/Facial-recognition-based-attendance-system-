from django.db import models
 
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    s3_image_url = models.URLField(blank=True, null=True)  # URL of the image in S3, can be added after upload
    created_at = models.DateTimeField(auto_now_add=True)