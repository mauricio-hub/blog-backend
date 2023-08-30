from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializer import PostSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'

