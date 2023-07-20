from django.db import models
from django.urls import reverse

class Shoe(models.Model):
    size = models.IntegerField()
    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture = models.URLField()
    # bin_id = models.IntegerField()

    def get_api_url(self):
        return reverse("api_show_shoe", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("manufacturer", "model_name")
 