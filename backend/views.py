from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Curator, PlayerTeam, Station, Task
from .serializers import (
    CuratorSerializer,
    PlayerTeamSerializer,
    StationSerializer,
    TaskSerializer,
)


class PlayerTeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PlayerTeam.objects.all()
    serializer_class = PlayerTeamSerializer

    @action(detail=True, methods=["post"])
    def add_score(self, request, pk=None):
        team = self.get_object()
        team.score += request.data["score"]
        team.save()
        return Response({"score": team.score})

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
