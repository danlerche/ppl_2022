from django import template
from library_programs.models import Event
from library_programs.models import EventCategory
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import datetime
from datetime import timedelta

register = template.Library()

@register.inclusion_tag('library_programs/all_upcoming_events.html', takes_context=True)
def all_upcoming_events(context):
    today = datetime.datetime.now()
    year = timedelta(days=365)
    all_events = Event.objects.all()

    return {
        'all_upcoming_events': Event.objects.filter(start_date__gte=today) | Event.objects.filter(until__gte=today),
        'request': context['request'],
    }
