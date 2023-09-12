from rest_framework import serializers
from .models import PlayerTeam, Curator, Station, StationOrder, Task


class PlayerTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerTeam
        fields = "__all__"


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = "__all__"


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class StationOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationOrder
        fields = "__all__"
