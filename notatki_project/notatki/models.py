from django.utils import timezone

from django.db import models
# Create your models here.
class Notatka(models.Model):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    autor = models.CharField(max_length=100)
    data_publikacji = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tytul