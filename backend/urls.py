from rest_framework import routers

from .views import PlayerTeamViewSet, CuratorViewSet, StationViewSet, TaskViewSet

router = routers.DefaultRouter()
# router.register(r"team", TeamViewSet)
router.register(r"playerteam", PlayerTeamViewSet, basename="playerteam")
router.register(r"curator", CuratorViewSet, basename="curator")
router.register(r"station", StationViewSet, basename="station")
router.register(r"task", TaskViewSet, basename="task")
