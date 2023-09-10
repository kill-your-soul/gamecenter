from django.contrib import admin
from .models import PlayerTeam, Curator, Station, Task
from django.utils import timezone

# Register your models here.


class PlayerTeamAdmin(admin.ModelAdmin):
    list_display = ("teamname", "score", "current_station")


class CuratorAdmin(admin.ModelAdmin):
    list_display = ("name", "station", "user")


class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "points", "task")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "question", "answer")


# admin.site.register(Person)
admin.site.register(PlayerTeam, PlayerTeamAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Task, TaskAdmin)
