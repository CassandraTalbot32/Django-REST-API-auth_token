from django import forms

from .models import PolicyForm


class PolicyForm(forms.ModelForm):
	Policy_reference = forms.CharField(label='',
						widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	Cover_type = forms.CharField()
	Car	= forms.CharField(
						required=False,
						widget=forms.Textarea(
							attrs={
							"placeholder": "Description",
							"class": "new-class-name two",
							"id": "my-id-for-textarea",
							"rows": 20,
							"cols": 100, 
							}
						)
					)
	Address = forms.CharField()
	
	

