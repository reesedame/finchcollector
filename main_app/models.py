from django.db import models
from django.urls import reverse


class Finch(models.Model):
    species = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    conservation_status = models.CharField(max_length=100)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})
