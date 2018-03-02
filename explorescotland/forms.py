from django import forms
from explorescotland.models import Feedback

class FeedbackForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):      #TODO find a way to get user 
    #     self.user = kwargs.pop('user')
    #     super(FeedbackForm, self).__init__(*args, **kwargs)

    message = forms.CharField(max_length=2000,
                                widget=forms.Textarea)
    # parent = self.user.ParentProfile
    class Meta:
        model = Feedback
        fields = ('message', )
