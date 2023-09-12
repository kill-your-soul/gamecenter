from rest_framework import routers
from django.urls import path, include

from .views import (
    PlayerTeamViewSet,
    CuratorViewSet,
    StationViewSet,
    TaskViewSet,
    StationOrderViewSet,
)

router = routers.DefaultRouter()
router.register(r"playerteam", PlayerTeamViewSet, basename="playerteam")
router.register(r"curator", CuratorViewSet, basename="curator")
router.register(r"station", StationViewSet, basename="station")
router.register(r"task", TaskViewSet, basename="task")
router.register(r"stationorder", StationOrderViewSet, basename="stationorder")

urlpatterns = [
    path(
        "playerteam/get_top_3/",
        PlayerTeamViewSet.as_view({"get": "get_top_3"}),
        name="playerteam-get-top-3",
    ),
    path("", include(router.urls)),
]
