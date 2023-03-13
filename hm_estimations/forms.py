from django import forms

class CommunicationRequestForm(forms.Form):
    email = forms.EmailField(label='Your Email Address')
    body = forms.CharField(label='Message', widget=forms.Textarea, required=True)


class EstimateForm(forms.Form):
    estimator_id = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    claim_num = forms.CharField(required=False)
    year = forms.CharField(required=False)
    make = forms.CharField(required=False)
    model = forms.CharField(required=False)
    images = forms.CharField(widget=forms.FileInput)
    notes = forms.CharField(widget=forms.Textarea)