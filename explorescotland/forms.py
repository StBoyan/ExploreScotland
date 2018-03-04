from django import forms
from explorescotland.models import Feedback

class FeedbackForm(forms.ModelForm):
    message = forms.CharField(max_length=2000,
                                widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ('message', )
