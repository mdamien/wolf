from django.shortcuts import render
from django.views import generic
from places.models import Pin, Category
from django import forms

def map(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            Pin.objects.get(pk=request.POST['pin_id']).delete()
        else:
            text = request.POST['text']
            lat = float(request.POST['lat'])
            lng = float(request.POST['lng'])
            cat = Category.objects.get(pk=request.POST['category'])
            pin = Pin(text=text, user=request.user, lat=lat, lng=lng, category=cat)
            pin.save()
    return render(request, 'places/map.html', {
        'pins':Pin.objects.all(),
        'categories':Category.objects.all()
    })

