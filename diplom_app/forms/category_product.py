from django import forms
from diplom_app.models import Business, Categories, Product

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"