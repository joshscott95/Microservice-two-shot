from django.db import models
from django.urls import reverse


class Hat(models.Model):
    fabric = models.CharField(max_length=255)
    style_name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    picture_url = models.URLField()
    # wardrobe_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hats')
    def get_api_url(self):
        return reverse("api_list_hat", kwargs={"pk": self.pk})

    def __str__(self):
        return self.style_name

    class Meta:
        ordering = ("style_name",)