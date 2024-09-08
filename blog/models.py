from django.db import models

# Create your models here.
class Aurthor(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()


class Article(models.Model):
    title = models.CharField(max_length=100)
    body =models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    aurthor = models.ForeignKey(Aurthor,on_delete=models.CASCADE)
