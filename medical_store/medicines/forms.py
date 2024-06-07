from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Medicine

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('name', 'description', 'price', 'quantity')
