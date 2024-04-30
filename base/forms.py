from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Manager, Seller

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'user_role')
class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'  # Or specify fields needed for the form

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'  # Or specify fields needed for the form