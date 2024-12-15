from django.db import models

class Perfume(models.Model):
    SIZE_CHOICES = [
        ("25 ml", "25 ml"),
        ("50 ml", "50 ml"),
        ("75 ml", "75 ml"),
    ]
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default="25 ml")
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=24.00)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def save(self, *args, **kwargs):
        """Set the price based on size before saving."""
        size_price_map = {
            "25 ml": 24.00,
            "50 ml": 36.00,
            "75 ml": 60.00,
        }
        self.price = size_price_map[self.size]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_gender_display()}) - {self.get_size_display()}"
