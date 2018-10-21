from django.db.models import Q
from rest_framework import filters

from flats.models import Flat
from houses.models import House

house_model = House
flat_model = Flat


class IsOwnerFlatFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        houses = house_model.objects.filter(user=request.user).only('id')

        condition = Q()
        for house in houses:
            condition |= Q(house_id=house.id)
        return queryset.filter(condition)
