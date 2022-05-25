#https://dateutil.readthedocs.io/en/stable/examples.html#rrule-examples
from django.db import models
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.core.fields import RichTextField


class EventAge(ClusterableModel):
    age_range = models.CharField(max_length=300, null=True, blank=True)
    color = ColorField(null=True, blank=True)

    panels = [
    FieldPanel('age_range'),
    NativeColorPanel('color'),
    ]

    def __str__(self):
        return self.age_range

class EventCategory(ClusterableModel):
    category_name = models.CharField(max_length=300, null=True, blank=True)
    color = ColorField(null=True, blank=True)

    panels = [
    FieldPanel('category_name'),
    NativeColorPanel('color'),
    ]

    def __str__(self):
        return self.category_name


REPEAT_TYPE = (
    ("DAILY", "Daily"),
    ("WEEKLY", "Weekly"),
    ("MONTHLY", "Monthly"),
    ("YEARLY", "Yearly"),
)

class Occurrence(models.Model):
    repeats = models.CharField(max_length = 20, choices = REPEAT_TYPE, null=True, blank=True)

    def __str__(self):
        return self.repeats

class Event(Page, Orderable):
    event_category = ParentalKey(EventCategory, on_delete=models.SET_NULL, related_name='event_category', null=True, blank=True)
    age_range = ParentalKey(EventAge, on_delete=models.SET_NULL, related_name='event_age', null=True, blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    time_from = models.TimeField(null=True)
    time_to = models.TimeField(null=True)
    description = RichTextField(max_length=1500,null=True,blank=True)
    repeats = models.ForeignKey(Occurrence, null=True, blank=True, verbose_name="repeat", on_delete=models.SET_NULL)
    until = models.DateField(null=True,blank=True)

    content_panels = [
    FieldPanel('title'),
    FieldPanel('event_category'),
    FieldPanel('age_range'),
    FieldPanel('start_date'),
    FieldPanel('end_date'),
    FieldPanel('time_from'),
    FieldPanel('time_to'),
    FieldPanel('description'),
    FieldPanel('repeats'),
    FieldPanel('until'),
    ]
