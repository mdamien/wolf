from django.shortcuts import render
from django.views import generic
from places.models import Pin
from django import forms


def map(request):
    if request.method == 'POST':
        text = request.POST['text']
        lat = float(request.POST['lat'])
        lng = float(request.POST['lng'])
        pin = Pin(text=text, user=request.user, lat=lat, lng=lng)
        pin.save()
    return render(request, 'places/map.html', {
        'pin_list':Pin.objects.all()
    })

