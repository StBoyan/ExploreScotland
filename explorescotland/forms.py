from django import forms
from explorescotland.models import Feedback
from django.contrib.auth.models import User

class FeedbackForm(forms.ModelForm):
    message = forms.CharField(max_length=2000,
                                widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ('message', )

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )
