from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ContainsASerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    queryset = Author.contains_a.all()
