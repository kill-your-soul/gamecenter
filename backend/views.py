from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# import apivewsset

from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
import random
import logging

from .models import Curator, PlayerTeam, Station, Task, StationOrder
from .serializers import (
    CuratorSerializer,
    PlayerTeamSerializer,
    StationSerializer,
    TaskSerializer,
    StationOrderSerializer,
)

logger = logging.getLogger(__name__)


class StationOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StationOrder.objects.all()
    serializer_class = StationOrderSerializer


class PlayerTeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PlayerTeam.objects.all()
    serializer_class = PlayerTeamSerializer

    @action(detail=True, methods=["post"])
    def add_score(self, request, pk=None):
        print(request.data)
        team = self.get_object()
        team.score += request.data["score"]
        team.current_station += 1
        # team.current_station = team.stations.
        team.save()
        return Response({"score": team.score, "current_station": team.current_station})

    @action(detail=True, methods=["post"])
    def set_current_station(self, request, pk=None):
        team = self.get_object()
        station = Station.objects.get(pk=request.data["current_station"])
        team.current_station = station
        team.save()
        logger.warning(team.current_station)
        return Response({"current_station": str(team.current_station)})

    @action(detail=True, methods=["get"])
    def get_top_3(self, request, pk=None):
        teams = self.get_queryset().order_by("-score")[:3]
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=False):
            all_stations = Station.objects.all()
            random_stations = random.sample(list(all_stations), 10)
            random.shuffle(random_stations)

            station_order = StationOrder.objects.create(
                first=random_stations[0],
                second=random_stations[1],
                third=random_stations[2],
                fourth=random_stations[3],
                fifth=random_stations[4],
                sixth=random_stations[5],
                seventh=random_stations[6],
                eighth=random_stations[7],
                ninth=random_stations[8],
                tenth=random_stations[9],
            )
            player_team = PlayerTeam.objects.create(
                user=request.user,
                teamname=request.data["teamname"],
                stations=station_order,
                current_station=random_stations[0],
            )

            # for order, station in enumerate(random_stations):
            #     player_team.stations.add(station, through_defaults={'order': order})

            player_team.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class UserApiViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def get_user(self, request):
        # logger.warning(request.headers["Authorization"].split(" ")[1])
        access_token = AccessToken(request.headers["Authorization"].split(" ")[1])
        try:
            pt = PlayerTeam.objects.get(user=access_token.payload["user_id"])
            logger.warning(pt)
        except:
            resp = Response(
                {
                    "user_id": access_token.payload["user_id"],
                    "is_curator": True,
                    "is_player": False,
                }
            )
        try:
            cur = Curator.objects.get(user=access_token.payload["user_id"])
            logger.warning(cur)
        except:
            resp = Response(
                {
                    "user_id": access_token.payload["user_id"],
                    "is_curator": False,
                    "is_player": True,
                }
            )
        # logger.warning(access_token)
        logger.warning(access_token.payload["user_id"])
        return resp
