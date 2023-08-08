from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Person, related_name="teams")

    def __str__(self):
        return self.name
