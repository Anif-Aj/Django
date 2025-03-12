from django.db import models

class Screenshot(models.Model):
    title = models.CharField(max_length=100)  # Optional: A title for the screenshot
    image = models.ImageField(upload_to='screenshots/')  # Path to save the screenshot
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
