from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)  # Optional subpage link
    order = models.PositiveIntegerField()  # Order of cards
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)
    background_color = models.CharField(max_length=7, blank=True, null=True)  # Hex color code

    def __str__(self):
        return self.title