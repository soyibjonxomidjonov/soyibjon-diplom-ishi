from django.contrib import admin
from .models import Categories, Product, Users, Orders, Business, Businessmen, OrderItems
# Register your models here.
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Users)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Business)
admin.site.register(Businessmen)