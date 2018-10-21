from django.http import Http404
from rest_framework import viewsets
from flats.filters import IsOwnerFlatFilterBackend
from flats.models import Flat
from flats.serializers import FlatSerializer
from houses.models import House

flat_model = Flat
house_model = House


class FlatViewSet(viewsets.ModelViewSet):
    serializer_class = FlatSerializer
    queryset = flat_model.objects.all()
    filter_backends = [IsOwnerFlatFilterBackend]

    def perform_create(self, serializer):
        house = serializer.validated_data['house']

        if self.request.user == house.user:
            return serializer.save(house=house)
        else:
            raise Http404

    def perform_update(self, serializer):
        flat = flat_model.objects.get(pk=self.kwargs['pk'])
        flat.schema.delete()
        return serializer.save()

    def perform_destroy(self, instance):
        instance.schema.delete()
        return instance.delete()
