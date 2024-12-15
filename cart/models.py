from django.db import models
from django.contrib.auth.models import User
from shop.models import Perfume


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=24.00)

    def save(self, *args, **kwargs):
        self.total_price = 24 * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.perfume.name} ({self.size}) x {self.quantity}"
