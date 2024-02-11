from django.db import models


class AtiyaProduct(models.Model):
    def __str__(self):
        return f"{self.name} ba mujudi {self.tedad} ba kod {self.kod}"

    name = models.CharField(max_length=50)
    berand = models.CharField(max_length=50)
    gheymat = models.IntegerField()
    rang = models.CharField(max_length=50)
    kod = models.IntegerField()
    tedad = models.IntegerField()
    size = models.IntegerField()
    enter = models.DateField()
