from django.shortcuts import render,redirect
from .models import Event , Booking
from .forms import Bookingform
# Create your views here.

def Home(request):
    return render(request,'home.html')
def about(rquest):
    return render(rquest,'about.html')
def contact(request):
    return render(request,'contact.html')
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)
def booking(request):
    if request.method=='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=Bookingform()
    dict_form = {
        'form' : form
    }
    return render(request,'booking.html',dict_form)
