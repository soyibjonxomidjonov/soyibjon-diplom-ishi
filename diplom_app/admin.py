from django.contrib import admin
from diplom_app.models import Category, Product, Users, Orders, Business, Businessmen, OrderItems
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Users)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Business)
admin.site.register(Businessmen)