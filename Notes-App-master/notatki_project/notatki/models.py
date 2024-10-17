from django.utils import timezone

from django.db import models
# Create your models here.

class Notatka(models.Model):

    POZIOM_WAZNOSCI = [
        ('malo', 'Mało ważny'),
        ('srednio', 'Średnio ważny'),
        ('bardzo', 'Bardzo ważny'),
    ]


    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    autor = models.CharField(max_length=100)
    data_publikacji = models.DateTimeField(default=timezone.now)
    poziom_waznosci = models.CharField(max_length=10, choices=POZIOM_WAZNOSCI, default='malo')

    def __str__(self):
        return self.tytul