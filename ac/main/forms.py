from django import forms

class MainForm(forms.Form):
    include = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'include',
            }
        ), required=False)
    exclude = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'exclude',
            }
        ), required=False)
