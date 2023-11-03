from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
class Posts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   
    created_at = models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    images=models.ImageField(upload_to='posts_images/')
    video=models.FileField(upload_to='videos/',blank=True, null=True)

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} лайкнул пост {self.post.id}"


