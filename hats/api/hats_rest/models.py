from django.db import models
from django.urls import reverse


class LocationVO(models.Model):
    closet_name = models.CharField(max_length=100)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()

    def to_dict(self):
        return {
            'id': self.id,
            'closet_name': self.closet_name,
            'section_number': self.section_number,
            'shelf_number': self.shelf_number,
        }

    def __str__(self):
        return f"{self.closet_name} - {self.section_number}/{self.shelf_number}"

    class Meta:
        ordering = ("closet_name", "section_number", "shelf_number")



class Hat(models.Model):
    fabric = models.CharField(max_length=255)
    style_name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    picture_url = models.URLField()
    wardrobe_location = models.ForeignKey(LocationVO, on_delete=models.CASCADE, related_name='hats', null=True)

    def to_dict(self):
        return {
            'id': self.id,
            'fabric': self.fabric,
            'style_name': self.style_name,
            'color': self.color,
            'picture_url': self.picture_url,
            'wardrobe_location': self.wardrobe_location.to_dict() if self.wardrobe_location else None,
        }
    
    def get_api_url(self):
        return reverse("api_list_hat", kwargs={"pk": self.pk})

    def __str__(self):
        return self.style_name

    class Meta:
        ordering = ("style_name",)
    
