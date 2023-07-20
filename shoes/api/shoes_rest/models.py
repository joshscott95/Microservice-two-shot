from django.db import models

class Shoe(models.Model):
    size = models.IntegerField()
    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture = models.URLField()
    # bin_id = models.IntegerField()
