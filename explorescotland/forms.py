from django import forms
from django.contrib.auth.models import userHomePage

class ParentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class ParentProfileForm(forms.ModelForm): # If ParentProfile is removed - this should go too
    class Meta:
        model = ParentProfile
