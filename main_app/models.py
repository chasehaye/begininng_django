from django.db import models
from django.urls import reverse

# Create your models here.
class Feed(models.Model):
  name = models.CharField(max_length=30)
  type = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('feeds_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    length = models.IntegerField()
    feeds = models.ManyToManyField(Feed)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Location(models.Model):
    climate = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Found in {self.climate} in {self.country}"