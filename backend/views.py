from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PlayerTeam, Curator, Station, Task

from .serializers import (
    PlayerTeamSerializer,
    CuratorSerializer,
    StationSerializer,
    TaskSerializer,
)


# class TeamViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer


class PlayerTeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PlayerTeam.objects.all()
    serializer_class = PlayerTeamSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class CuratorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer

    def get_queryset(self):
        return self.queryset.filter(curator=self.request.user)


class StationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def get_queryset(self):
        return self.queryset.filter(station=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.queryset.filter(task=self.request.user)
