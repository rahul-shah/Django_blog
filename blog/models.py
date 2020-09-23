from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce import HTMLField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    title = models.CharField(max_length = 50000)
    text = HTMLField('Content')
    image = models.FileField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

def publish(self):
    self.published_date = timezone.now
    self.save()

def __str__(self):
    return self.title
