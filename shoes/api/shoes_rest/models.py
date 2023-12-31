from django.db import models
from django.urls import reverse


class BinVO(models.Model):
   closet_name = models.CharField(max_length=100)
   bin_number = models.PositiveSmallIntegerField()
   bin_size = models.PositiveSmallIntegerField()
   import_href = models.CharField(max_length=100)


class Shoe(models.Model):
    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    shoe_color = models.CharField(max_length=200)
    picture = models.URLField()

    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.CASCADE,
    )

    def get_api_url(self):
        return reverse("api_show_shoe", kwargs={"pk": self.pk})

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ("manufacturer", "model_name")
