from django.db import models
# from django import forms

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.title
