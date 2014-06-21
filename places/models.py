from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pin(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    category = models.ForeignKey(Category)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
