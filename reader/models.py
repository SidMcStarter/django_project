from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images")