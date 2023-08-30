from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from post.models import Post
from post.api.serializer import PostSerializer
from post.api.permissions import IsAdminOrReadOnly
class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    # filtro por category id
    #filterset_fields = ['category']
    #filtro por slug
    filterset_fields = ['category__slug']

