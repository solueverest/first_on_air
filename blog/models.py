from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_published = models.DateTimeField()
