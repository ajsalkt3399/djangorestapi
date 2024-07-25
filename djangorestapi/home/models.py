from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.team_name

# Create your models here.
class Person(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name="members")
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=100)