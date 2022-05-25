from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import (EventCategory,Event,EventAge,Occurrence)


class EventCategoryAdmin(ModelAdmin):
    model = EventCategory
    menu_label = 'Event Category'
    menu_icon = 'list-ul'

class EventAgeAdmin(ModelAdmin):
    model = EventAge
    menu_label = 'Age Range'
    menu_icon = 'list-ul'

#class EventAdmin(ModelAdmin):
#    model = Event
#    menu_label = 'Event'
#    menu_icon = 'date'
#    list_filter = ('event_category_id', 'age_range_id' )


class OccurrenceAdmin(ModelAdmin):
    model = Occurrence
    menu_label = 'Occurrence'
    menu_icon = 'time'

class EventAdminGroup(ModelAdminGroup):
    menu_label = 'Programs & Events'
    menu_icon = 'date'
    menu_order = 200
    items = (EventCategoryAdmin, EventAgeAdmin, OccurrenceAdmin)

modeladmin_register(EventAdminGroup)
