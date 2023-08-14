from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PlayerTeam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teamname = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.teamname


class Curator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    task = models.ForeignKey("Task", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
