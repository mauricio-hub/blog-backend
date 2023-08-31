from django.db import models
from django.db.models import CASCADE
from post.models import Post
from users.models import User

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # cuando se elimine un post, se eliminen todos los comentarios que haya hecho
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, null=True)
    # cuando se elimine un usuario, se eliminen todos los comentarios que haya hecho
    user = models.ForeignKey('users.User', on_delete=models.CASCADE , null=True)

    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-created_at']
