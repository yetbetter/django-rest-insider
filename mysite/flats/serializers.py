from rest_framework import serializers

from flats.models import Flat


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = (
            'schema',
            'house',
            'price',
            'number',
            'entrance',
            'floor',
            'status',
            'type'
        )
        many = True
