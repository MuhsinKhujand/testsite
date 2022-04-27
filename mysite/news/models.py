from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%M/', width_field=400, height_field=400, verbose_name="photo")
    is_published = models.BooleanField(default=True)
    email = models.EmailField(null=True)
