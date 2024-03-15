from datetime import datetime

from django import forms

class ChoiceForm(forms.Form):
    choice = forms.ChoiceField(choices=[('D', 'Монета'), ('N', 'Число')],
                      widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    count = forms.IntegerField(min_value=1, max_value=100)

