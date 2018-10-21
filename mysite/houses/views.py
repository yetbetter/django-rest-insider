from django.http import Http404
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from flats.models import Flat
from flats.serializers import FlatSerializer
from houses.filters import IsOwnerHouseFilterBackend
from houses.models import House
from houses.serializers import HouseSerializer

house = House
flat = Flat


class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = house.objects.all()
    filter_backends = [IsOwnerHouseFilterBackend]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class HouseFlatsListView(ListAPIView):
    serializer_class = FlatSerializer
    queryset = flat.objects.all()

    def get_queryset(self):
        is_user_house = house.objects.filter(
            user_id=self.request.user.id
        ).filter(
            id=self.kwargs['id']
        ).exists()

        if is_user_house:
            return flat.objects.filter(house_id=self.kwargs['id'])
        else:
            raise Http404()
