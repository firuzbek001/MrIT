from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class TranslatedItem(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name