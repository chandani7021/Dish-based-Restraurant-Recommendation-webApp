from django.db import models

# Dish model.
class Dish (models.Model):

    name = models.CharField(("name"), max_length = 255)
    location = models.CharField(("location"), max_length = 255)
    items = models.TextField(("items"))

    def __str__(self):
        return self.name