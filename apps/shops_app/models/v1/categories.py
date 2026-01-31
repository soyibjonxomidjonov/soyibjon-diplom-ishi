from django.db import models
from diplom_app.models.v1.people_models import Businessmen
from django.utils.text import slugify



class Business(models.Model):
    business_owner = models.ForeignKey(Businessmen, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='business_logos/%Y/%m/%d/', null=True, blank=True)
    business_info = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.business_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.business_name

class Category(models.Model):
    name = models.CharField(max_length=300)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

