from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(label='Your Name (required)', max_length=250)
    email = forms.EmailField(label='Your Email (required)')
    subject = forms.CharField(max_length=250, required=False)
    message = forms.CharField(label='Message (required)', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name (required)'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email (required)'
        self.fields['message'].widget.attrs['placeholder'] = 'Message (required)'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'