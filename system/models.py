from django.db import models


class Person(models.Model):
    title = models.CharField("name", max_length=255)
    age = models.PositiveIntegerField("age")
    address = models.TextField("address")

    def __str__(self):
        return self.title