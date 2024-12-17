from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'


class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets={
            'booking_date' : DateInput()
        }
        
        labels={
            'custmer_name' : 'Customer Name',
            'phonenumber'  : 'Phone Number',
            'event_name'   : 'Event Name',
            'booking_date' : 'Booking Date',
            
        }