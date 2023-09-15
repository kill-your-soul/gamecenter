from django.contrib import admin
from .models import PlayerTeam, Curator, Station, Task, StationOrder
from django.utils import timezone
import random
import logging

# Get a logger instance for your module
logger = logging.getLogger(__name__)

# Register your models here.


def generate_random_station_order(modeladmin, request, queryset):
    logger.warning(f"Generating random station order for teams {queryset}")
    for team in queryset:
        all_stations = Station.objects.all()
        # TODO: get 10 random stations instead of 3
        random_stations = random.sample(list(all_stations), 10)
        random.shuffle(random_stations)
        # TODO: create a station order with the 10 random stations
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
        team.stations = station_order
        team.current_station = random_stations[0]
        team.save()
        del all_stations


generate_random_station_order.short_description = (
    "Generate random station order for team"
)


class PlayerTeamAdmin(admin.ModelAdmin):
    list_display = ("teamname", "score", "current_station", "id")
    actions = [generate_random_station_order]


class CuratorAdmin(admin.ModelAdmin):
    list_display = ("name", "station", "user")


class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "points", "task", "id")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "question", "answer")


class StationOrderAdmin(admin.ModelAdmin):
    list_display = (
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
    )


# admin.site.register(Person)
admin.site.register(PlayerTeam, PlayerTeamAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(StationOrder, StationOrderAdmin)
