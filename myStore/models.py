from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    developer = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    abstract = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name
