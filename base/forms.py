from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Manager, Seller

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Manager, Seller

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'user_role')
        success_url = '/dashboard/'
class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'  


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'  

        