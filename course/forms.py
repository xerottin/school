from django import forms

from .models import *


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'more-text',

    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'more-text',
    }))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'more-text',
    }))

    class Meta:
        course = Course
        model = Student
        fields = ['name', 'last_name', 'phone_number']


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Write your comment ...'}),
                           label='Write review text')

    class Meta:
        model = Review
        fields = ['text']
