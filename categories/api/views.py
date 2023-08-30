from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

class CategoryViewSet(ModelViewSet):
    #  permisos para la api
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #  esto es lo que se va a mostrar en la api publicadas y no publicadas 
    # queryset = Category.objects.all()
    #  esto es lo que se va a mostrar en la api solo las publicadas
    queryset = Category.objects.filter(published=True)
    # serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # buscar por slug
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    #  filtrar por nombre
    filterset_fields = ['published', 'title', 'slug', 'created_at']