from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='nazvanie')
    content = models.TextField(blank=True, verbose_name='kontent')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='sozdan')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='obnavlyon')
    url_height = models.PositiveIntegerField()
    url_width = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/', width_field='url_width', height_field='url_height',
                              verbose_name="foto", blank=True)
    is_published = models.BooleanField(default=True, verbose_name='opublikovan')
    email = models.EmailField(null=True, verbose_name='e-pochta')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Novost'
        verbose_name_plural = 'Novosti'
        ordering= ['-created_at']
