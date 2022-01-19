from django.db.models.base import Model
from rest_framework import serializers
from core.models import Editora
from core.serializers import EditoraSerializer
from rest_framework.viewsets import ModelViewSet


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
