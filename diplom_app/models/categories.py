from django.db import models
from .people_models import Businessmen
from django.utils.text import slugify



class Business(models.Model):
    business_owner = models.ForeignKey(Businessmen, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    business_type = models.CharField(max_length=100)
    business_info = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.business_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.business_name

class Categories(models.Model):
    name = models.CharField(max_length=300)
    businessman = models.ForeignKey(Businessmen, null=True, on_delete=models.PROTECT)
    business = models.ForeignKey(Business, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

