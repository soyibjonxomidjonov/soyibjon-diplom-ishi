from django import forms
from diplom_app.models import Businessmen, Users

class BusinessmenForm(forms.ModelForm):
    class Meta:
        model = Businessmen
        fields = "__all__"

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"