from django.contrib import admin
from .models import PlayerTeam, Curator, Station, Task

# Register your models here.


# admin.site.register(Person)
admin.site.register(PlayerTeam)
admin.site.register(Curator)
admin.site.register(Station)
admin.site.register(Task)
