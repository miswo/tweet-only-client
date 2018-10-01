from django import forms

class TestForm(forms.Form):
    words = forms.CharField(label='ツイート')