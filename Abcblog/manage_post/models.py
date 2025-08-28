from django.db import models # type: ignore
from django.contrib.auth import get_user_model # type: ignore
User = get_user_model() # type: ignore
from ckeditor.fields import RichTextField # pyright: ignore[reportMissingImports]

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Categories', blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=40)
    feature = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Artículo
class Article(models.Model):
    title = models.CharField(max_length=255)
    introducción = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField(upload_to='Articles', blank=False, null=False)
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

# Calificaciones
class Rating(models.Model):
    value = models.FloatField()
    description = models.CharField(max_length=255)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'