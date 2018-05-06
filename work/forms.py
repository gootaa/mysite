from django import forms

class MessageForm(forms.Form):
	name = forms.CharField(label='Your Name (required)', max_length=250)
	email = forms.EmailField(label='Your Email (required)')
	subject = forms.CharField(max_length=250, required=False)
	message = forms.CharField(label='Message (required)', widget=forms.Textarea)