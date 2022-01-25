from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.name, self.last_name)