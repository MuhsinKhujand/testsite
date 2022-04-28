from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url_height = models.PositiveIntegerField()
    url_width = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%M/', width_field='url_width', height_field='url_height', verbose_name="photo")
    is_published = models.BooleanField(default=True)
    email = models.EmailField(null=True)


    def __str__(self):
        return self.title

