from django.db import models


class Data(models.Model):
    label = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.label