from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadOnly

class CommentViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']  # Orden descendente (lo más reciente primero)
    filterset_fields = ['post']  # Filtrar por post

