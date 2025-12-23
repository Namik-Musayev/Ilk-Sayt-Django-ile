from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20, blank=True)
    url = models.CharField(max_length=255, default='#')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    amount = models.CharField(max_length=100)
    url = models.CharField(max_length=255, default='#')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    excerpt = models.TextField()
    url = models.CharField(max_length=255, default='#')

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    span = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=255)
    lead = models.TextField()
    text = models.TextField()
    link = models.URLField()
    link_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    icon = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.icon

class FooterLink(models.Model):
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Button(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.id

class Navigation(models.Model):
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class SliderImage(models.Model):
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.image
