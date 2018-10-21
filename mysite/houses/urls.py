from django.urls import path
from rest_framework import routers

from houses.views import HouseViewSet, HouseFlatsListView

router = routers.SimpleRouter()
router.register(r'houses', HouseViewSet)
urlpatterns = router.urls

urlpatterns.append(path('house/<int:id>/flats/', HouseFlatsListView.as_view()))
