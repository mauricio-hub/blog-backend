from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category
from django.contrib.postgres.fields import ArrayField 
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    miniature = models.ImageField(upload_to='post/images')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    

    def __str__(self):
        return self.title
