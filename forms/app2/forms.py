from django import forms

#Write your form here

class ContactForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Write your Name'
            }
        ))
    contact_email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Write your Email'
            }
        ))
    contact_number = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write your Number'
            }
        ))
    contact_content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Write your Message'
            }
        ))
