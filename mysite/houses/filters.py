from rest_framework import filters


class IsOwnerHouseFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user_id=request.user.id)