from django.db import models


class SampleImageModel(models.Model):
    contents_image = models.ImageField(blank=True)
