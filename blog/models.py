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

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')


class ContactModel(models.Model):
    name = models.CharField(max_length=50,default=None)
    email = models.EmailField(max_length=50,default=None)
    message = models.TextField(max_length=1000,default=None)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + "\t" + str(self.email) + "\t" + str(self.time)
