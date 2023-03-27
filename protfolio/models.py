import uuid
from django.db import models
from autoslug import AutoSlugField



class Profile(models.Model):
    title = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=14)
    upload = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", default="",unique=True, null=False)

    class Meta:
        verbose_name_plural = "Profile"
        ordering = ['-created_at']
