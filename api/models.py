from django.db import models



class Metar(models.Model):
    """ Create data model for metar """
    station = models.CharField(max_length=10)
    last_observation = models.DateTimeField(auto_now_add=True)
    temperature = models.CharField(max_length=50)
    wind = models.CharField(max_length=50)

    def __str__(self):
        return str(self.last_observation)+str(self.station)