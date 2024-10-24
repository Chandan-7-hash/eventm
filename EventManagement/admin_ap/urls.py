from django.urls import path
from admin_ap.views import *

urlpatterns = [
    path('', home, name='home')
    path('create', create_event, name='create_event'),
    path('event_li', event_list, name='event_list'),
    path('events_d', event_detail, name='event_detail'),
    path('events_up', update_event, name='update_event'),
    path('events_del', delete_event, name='delete_event')
]
