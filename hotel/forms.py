from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'description','hotel_main_image','price','offer']
