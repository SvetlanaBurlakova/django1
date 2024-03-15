from datetime import datetime

from django import forms

from myapp3.models import Author


class AuthorForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField()
    biography =forms.CharField(widget=forms.Textarea)
    birthdate = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}
    ))


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField()
    #date_publication = forms.DateField(auto_now_add=True)
    #author = forms.ModelChoiceField(queryset=Author.objects)
    #author = forms.ModelChoiceField(queryset=Author.objects.all())
    is_published = forms.BooleanField()
    views = forms.IntegerField()