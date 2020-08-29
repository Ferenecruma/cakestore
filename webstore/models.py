from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='categories')

    def __str__(self):
        return str(self.title)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Metadata(models.Model):
    facebook_link = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=200)
    addres = models.CharField(max_length=200)

class Post(models.Model):
    text = models.CharField(max_length=300)
