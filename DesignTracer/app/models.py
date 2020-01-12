from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=150)
    theme = models.TextField(blank=True)
    break_down = models.TextField(blank=True)
    key_point = models.TextField(blank=True)
    image_f = models.ImageField(upload_to='../images')
    created_at = models.DateTimeField(auto_now=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
