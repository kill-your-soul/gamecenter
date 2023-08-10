from rest_framework import routers
from .views import TeamViewSet

router = routers.DefaultRouter()
router.register(r"team", TeamViewSet)
