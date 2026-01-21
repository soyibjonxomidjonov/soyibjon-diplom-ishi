from django.db import models
from django.core.exceptions import ValidationError
from .people_models import Users
from .products import Product


class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    miqdor = models.IntegerField()
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # 1. Validatsiyani shu yerda bajaring
        if self.miqdor > self.product.maxsulot_soni:
            raise ValidationError("Omborda yetarli mahsulot yo'q!")

    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Zakaz {self.product.name} dan {self.miqdor} {self.product.maxsulot_birligi} oldi. {self.user.username.title()}"



class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order ID {self.order.id}"





































