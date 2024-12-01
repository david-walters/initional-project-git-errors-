from django.db import models

class Perfume(models.Model):
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=[("25 ml", "25 ml"), ("50 ml", "50 ml"), ("100 ml", "100 ml")], default="25 ml")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name} ({dict(self.SIZE_CHOICES).get(self.size, 'small')})"
    
    