from django.db import models

class airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class flight(models.Model):
    origin = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}:From {self.origin} to {self.destination}"

class passanger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flight = models.ManyToManyField(flight, blank=True, related_name="passangers")

    def __str__(self):
        return f"{self.first} {self.last}"

