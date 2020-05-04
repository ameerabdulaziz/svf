from django.conf import settings
from django.db import models
from django.urls import reverse
from location_field.models.plain import PlainLocationField


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='posts')
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['region'], zoom=7)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.publisher =

    # @models.permalink
    def get_absolute_url(self):
        return reverse('posts:post-detail', args=(self.id,))
