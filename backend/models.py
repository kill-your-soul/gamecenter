from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PlayerTeam(models.Model):
    # TODO: add start time
    # user = models.ManyToManyField(User, on_delete=models.CASCADE)
    teamname = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True, default=0)
    stations = models.ManyToManyField("Station", blank=True)

    def __str__(self):
        return self.teamname


class Curator(models.Model):
    # TODO: add station
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Station(models.Model):
    # TODO: add time and points
    time = models.IntegerField(blank=True, null=True, default=0)
    points = models.IntegerField(blank=True, null=True, default=0)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    assignment = models.TextField(blank=True, null=True)
    task = models.ForeignKey("Task", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
