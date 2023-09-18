from rest_framework.serializers import ModelSerializer


class SerializeAnnotationsMixin(ModelSerializer):
    def get_fields(self):
        fields = super().get_fields()
        for name, annotation in self.get_annotations().items():
            fields[name] = self.create_field(annotation)
        return fields

    def create_field(self, annotation):
        serializer_class = self.serializer_field_mapping[
            annotation.output_field.__class__
        ]
        return serializer_class(required=False, read_only=True)

    def get_annotations(self):
        if not hasattr(self, "annotations"):
            self.annotations = self.Meta.model._default_manager.all()._query.annotations
        return self.annotations
