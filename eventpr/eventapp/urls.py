from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="home"),
    path('about/',views.about,name="about"),
    path('booking/',views.booking,name="booking"),
    path('contact/',views.contact,name="contact"),
    path('events/',views.events,name="events"),
]
