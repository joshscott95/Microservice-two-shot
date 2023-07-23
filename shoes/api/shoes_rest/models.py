from django.db import models
from django.urls import reverse


class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()

    def to_dict(self):
        return {
            'id': self.id,
            'closet_name': self.closet_name,
            'bin_number': self.bin_number,
            'bin_size': self.bin_size,
        }

    def get_api_url(self):
        return reverse("api_bin", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.closet_name} - {self.bin_number}/{self.bin_size}"

    class Meta:
        ordering = ("closet_name", "bin_number", "bin_size")


class Shoe(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    picture = models.URLField()
    # bin = models.ForeignKey(BinVO, on_delete=models.CASCADE, related_name="shoes")

    def __str__(self):
        return f"{self.manufacturer} {self.model_name}"

    def to_dict(self):
        return {
            "id": self.id,
            "manufacturer": self.manufacturer,
            "model_name": self.model_name,
            "color": self.color,
            "picture": self.picture,
            # 'wardrobe_bin': self.wardrobe_bin.to_dict() if self.wardrobe_bin else None,
        }