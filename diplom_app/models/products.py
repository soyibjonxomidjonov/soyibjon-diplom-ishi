from django.db import models
from .categories import Categories, Business

UNIT_CHOICES = [
    ('kg', 'Kilogramm'),
    ('dona', 'Dona/Shtat'),
    ('litr', 'Litr'),
    ('metr', 'Metr'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    business_turi = models.ForeignKey(Business, on_delete=models.CASCADE)
    info = models.TextField()
    price = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/')
    maxsulot_soni = models.IntegerField(default=0)
    maxsulot_birligi = models.CharField(max_length=10, choices=UNIT_CHOICES, default='dona')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def maxsulot_bormi(self):
        return self.maxsulot_soni > 0

    def maxsulotni_kamaytirish(self, quantity):
        if quantity > self.maxsulot_soni:
            return False

        self.maxsulot_soni -= quantity
        self.save()
        return True

    def maxsulot_qoshish(self, amount):
        self.maxsulot_soni += amount
        self.save()

    class Meta:
        ordering = ['name']