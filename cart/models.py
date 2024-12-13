from django.db import models
from django.contrib.auth.models import User
from shop.models import Perfume


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.perfume.name} ({self.size}) x {self.quantity}"
