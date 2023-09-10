from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import random

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
        print(request.data)
        team = self.get_object()
        team.score += request.data["score"]
        print(team.stations.all())
        # team.current_station = team.stations.
        team.save()
        return Response({"score": team.score})

    @action(detail=True, methods=["get"])
    def get_top_3(self, request, pk=None):
        teams = self.get_queryset().order_by("-score")[:3]
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        all_stations = Station.objects.all()
        random_stations = random.sample(list(all_stations), 2)
        random.shuffle(random_stations)
        station_order = [station.id for station in random_stations]

        print(random_stations[0])
        print(random_stations)
        serializer.save(stations=station_order, current_station=random_stations[0])
        print(serializer.data)
        return Response(serializer.data)


class CuratorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer


class StationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
