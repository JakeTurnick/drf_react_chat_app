from django.db import models
from django.conf import settings

# Create your models here.


class Chat_room(models.Model):
    title = models.CharField(max_length=255)
    # creator = models.CharField(max_length=255)
    # members = models.TextField()

    def __str__(self):
        return self.title


class Chat_message(models.Model):
    room = models.ForeignKey(Chat_room, on_delete=models.CASCADE)
    text = models.TextField()
    # author = models.ForeignKey(
    #     user, settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.text[:50]

# class User(models.Model):
