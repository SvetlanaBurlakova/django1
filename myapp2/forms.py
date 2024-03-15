from datetime import datetime

from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField()
    image = forms.ImageField()



