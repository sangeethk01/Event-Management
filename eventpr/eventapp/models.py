from django.db import models

# Create your models here.
class Event(models.Model):
    image =models.ImageField(upload_to="pic")
    name =models.CharField(max_length=200)
    desc =models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    custmer_name = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=12)
    event_name = models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    
