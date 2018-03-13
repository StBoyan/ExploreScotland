from django import forms
from explorescotland.models import Feedback, ParentProfile, ChildProfile
from django.contrib.auth.models import User
from django.forms import extras, SelectDateWidget
import datetime

class FeedbackForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ('message', )

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name',
                                required=False)
    last_name = forms.CharField(label='Last Name',
                                required=False)
    email = forms.EmailField(label='Email',
                                required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(required=False,
                                choices=ParentProfile.GENDER_CHOICES)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, datetime.datetime.now().year)),
                                label='Date of birth', required=False)

    class Meta:
        model = ParentProfile
        fields = ('birthdate', 'gender')

class ChildForm(forms.ModelForm):
    name  = forms.CharField(label='Child Name')

    class Meta:
        model = ChildProfile
        fields = ('name', )
