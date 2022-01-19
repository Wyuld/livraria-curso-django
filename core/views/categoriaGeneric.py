from core.models import Categoria
from core.serializers import CategoriaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriasDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"  ## Forçando que o campo de busca seja o ID
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
