from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    no_of_pages = models.IntegerField()
    date_published = models.DateField()
    quantity = models.IntegerField()


    def __str__(self):
        return self.title
