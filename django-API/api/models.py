from django.db import models

class Krosovka(models.Model):
    brand = models.CharField(max_length=100)
    size = models.IntegerField(default=10)
    color = models.CharField(max_length=30)
    price = models.IntegerField(default=40)
    
    def __str__(self):
        return f"brand: {self.brand}"
