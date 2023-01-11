from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Name', 'Phone_number', 'District', 'Activity', 'Amount')

        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),
            'Phone_number' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'District' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'District'}),
            'Activity' : forms.Select(attrs={'class':'form-select', 'placeholder':'Activity'}),
            'Amount' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Amount'})

        }