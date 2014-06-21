from django.db import models
from django.contrib.auth.models import User

class Pin(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
