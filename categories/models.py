from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # esta funcion es para que cuando se cree una nueva categoria, se muestre el titulo de la categoria
    def __str__(self):
        return self.title

