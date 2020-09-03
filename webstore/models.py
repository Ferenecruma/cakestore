from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=40, unique=False, editable=False)
    description = models.TextField()
    photo = models.ImageField(upload_to='categories')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, to_lower=True)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=40, unique=False, editable=False)
    description = models.TextField()
    photo = models.ImageField(upload_to='sub_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Підкатегорія'
        verbose_name_plural = 'Підкатегорії'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, to_lower=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class Metadata(models.Model):
    facebook_link = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=200)
    addres = models.CharField(max_length=200)


class Post(models.Model):
    text = models.CharField(max_length=300)
