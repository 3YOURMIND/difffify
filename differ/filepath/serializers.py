import json

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from filepath.models import FilePath, Tag


class TagsRelatedField(serializers.StringRelatedField):
    def to_internal_value(self, data):
        try:
            return Tag.objects.get(name=data)
        except Tag.DoesNotExist:
            return Tag.objects.create(name=data)


class FilePathSerializer(serializers.ModelSerializer):
    tags = TagsRelatedField(many=True)
    additionalInfo = serializers.CharField(source='additional_info_json')

    class Meta:
        model = FilePath
        fields = ('id', 'path', 'tags', 'additionalInfo')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['additionalInfo'] = json.loads(
            instance.additional_info_json
        )
        return representation

    def to_internal_value(self, data):
        if 'additionalInfo' not in data:
            raise ValidationError(
                {'additionalInfo': 'This field is required.'}
            )
        try:
            if not isinstance(data['additionalInfo'], dict):
                raise ValueError()
            data['additionalInfo'] = json.dumps(data['additionalInfo'])
        except ValueError:
            raise ValidationError(
                {'additionalInfo': 'This field must be a dictionary'}
            )
        return super().to_internal_value(data)
