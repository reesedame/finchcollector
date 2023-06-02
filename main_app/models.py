from django.db import models
from django.urls import reverse

FOOD_TYPES = (("W", "Worm"), ("B", "Berry"), ("S", "Seed"))


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("locations_list")


class Finch(models.Model):
    species = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    conservation_status = models.CharField(max_length=100)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})


class Feeding(models.Model):
    date = models.DateField("Feeding date")
    food_type = models.CharField(
        max_length=1, choices=FOOD_TYPES, default=FOOD_TYPES[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Fed {self.get_food_type_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
