from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    events = Event.objects.all()  
    services = Service.objects.all()  
    pricings = Pricing.objects.all()  
    reviews = Review.objects.all()  
    d = {'events': events, 'services': services, 'pricings': pricings, 'reviews': reviews}
    return render(request, 'index.html',d)

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        d = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', d)

def event_list(request):
    events = Event.objects.all()  
    d = {'events': events}
    return render(request, 'event_list.html')

def event_detail(request, event_id):
    EO = Event.objects.get(id=event_id)
    d = {'event': EO}
    return render(request, 'event_detail.html',d)

def update_event(request, event_id):
    EO = Event.objects.get(eve = event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=EO)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=EO.id)
    else:
        form = EventForm(EO)
        d = {'form': form}
    return render(request, 'update_event.html', d)

def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        d = {'event': event}
        event.delete()
        return redirect('event_list')
    return render(request, 'delete_event.html', d)
