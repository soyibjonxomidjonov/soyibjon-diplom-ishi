from django import forms
from diplom_app.models import Users



class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'password', 'phone_number', 'is_businessman']
        first_name = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control',
            })
        )
        last_name = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control',
            })
        )
        username = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control',
            })
        )
        password = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
            })
        )
        phone_number = forms.CharField(
            widget=forms.NumberInput(attrs={
                'class': 'form-control',
            })
        )
        is_businessman = forms.BooleanField(
            label="Siz biznesmenmisiz?",
            required=False,
            widget=forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            })
        )



class LoginForm(forms.Form):
    username = forms.CharField(label="Foydalanuvchi nomi", widget=forms.TextInput(attrs={'class': "form-input"}))
    password = forms.CharField(label="Parolingizni kiriting", widget=forms.PasswordInput(attrs={'class': "form-input"}))

















