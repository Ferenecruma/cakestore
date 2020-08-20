from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
