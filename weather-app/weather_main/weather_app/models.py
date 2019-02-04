from django.db import models


class Weather(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    wind_speed = models.IntegerField(default=0)
    high_temp = models.IntegerField(default=0)
    min_temp = models.IntegerField(default=0)
    rain = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.date
