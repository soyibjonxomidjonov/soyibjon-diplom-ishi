from django import forms
from diplom_app.models import Business, Category, Product

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'image', 'business_info']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'
                                                    }),

            'business_info': forms.Textarea(attrs={'class': 'form-control',
                                                   'rows': 4,
                                                   'cols': 40,
                                                   }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),

        }
        label = {
            'business_name': 'Biznes nomi',
            'image': 'Biznes logotipi',
            'business_info': 'Biznes haqida ma\'lumot',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Category.objects.all().order_by('name')
        self.fields['parent'].empty_label = "---- Asosiy kategoriyani tanlang---"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'info', 'image', 'category', 'business_turi', 'maxsulot_soni', 'maxsulot_birligi']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'info': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'business_turi': forms.Select(attrs={'class': 'form-select'}),
            'maxsulot_soni': forms.NumberInput(attrs={'class': 'form-control'}),
            'maxsulot_birligi': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all().order_by('name')
        self.fields['category'].empty_label = "Kategoriyani tanlang ^"
        if user:
            self.fields['business_turi'].queryset = Business.objects.filter(business_owner=user)
        self.fields['business_turi'].empty_label = "Biznes turini tanlang ^"






























