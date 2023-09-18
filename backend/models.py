from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Station(models.Model):
    time = models.DurationField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True, default=0)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    assignment = models.TextField(blank=True, null=True)
    task = models.ForeignKey("Task", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class StationOrder(models.Model):
    first = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="first_station",
    )
    second = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="second_station",
    )
    third = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="third_station",
    )
    fourth = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="fourth_station",
    )
    fifth = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="fifth_station",
    )
    sixth = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="sixth_station",
    )
    seventh = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="seventh_station",
    )
    eighth = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="eighth_station",
    )
    ninth = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="ninth_station",
    )
    tenth = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="tenth_station",
    )

    def __str__(self):
        return f"{self.first} {self.second} {self.third} {self.fourth} {self.fifth} {self.sixth} {self.seventh} {self.eighth} {self.ninth} {self.tenth}"


class PlayerTeam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teamname = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True, default=0)
    # stations = ArrayField(models.ForeignKey("Station", on_delete=models.CASCADE), null=True, blank=True)
    # stations = models.ManyToManyField(Station, blank=True, through=PlayerTeamStation)
    stations = models.ForeignKey(
        "StationOrder", on_delete=models.CASCADE, blank=True, null=True
    )
    current_station = models.ForeignKey(
        "Station",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="current_station",
    )

    def __str__(self):
        return self.teamname


class Curator(models.Model):
    station = models.ForeignKey(
        "Station", on_delete=models.CASCADE, blank=True, null=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
