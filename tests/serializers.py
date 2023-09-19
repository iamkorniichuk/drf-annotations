from rest_framework import serializers
from src.drf_annotations.mixins import SerializeAnnotationsMixin

from .models import Author


class AuthorSerializer(SerializeAnnotationsMixin, serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ContainsASerializer(SerializeAnnotationsMixin, serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    queryset = Author.contains_a.all()
