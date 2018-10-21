from rest_framework import serializers


class PricesSerializer(serializers.Serializer):
    price = serializers.FileField()
    house_id = serializers.IntegerField()

