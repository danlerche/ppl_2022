from django.db import models
from datetime import datetime
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.core import blocks
from wagtail.core.blocks import StaticBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import (
  CharBlock, PageChooserBlock, StructValue, StructBlock, TextBlock, URLBlock, EmailBlock, BooleanBlock)
from open_hours.models import OpenHour


@register_snippet
class Logo(models.Model):
    logo_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    logo_label = 'Logo'

    panels = [
       ImageChooserPanel('logo_image', classname="full"),
    ]

    def __str__(self):
        return self.logo_label

@register_snippet
class Alert(Orderable):
    enable_alert = models.BooleanField(default=False)
    alert_date = models.DateTimeField(default=datetime.now)
    alert_text = RichTextField(blank=True)
    alert_label = 'Alert'
    COLOURS = (
    ('R', 'Red'),
    ('G', 'Green'),
    )
    alert_colour = models.CharField(max_length=1, choices=COLOURS, default='G')

    panels = [
        FieldPanel('enable_alert'),
        FieldPanel('alert_date'),
        FieldPanel('alert_text'),
        FieldPanel('alert_colour'),
    ]

    def __str__(self):
        return self.alert_label


class TelephoneBlock(blocks.StructBlock):
        telephone = blocks.CharBlock(classname="telephone")
        class Meta:
            template = 'header_footer/blocks/telephone.html'

class HeadingBlock(blocks.StructBlock):
        heading = blocks.CharBlock(classname="heading")
        class Meta:
            template = 'header_footer/blocks/heading.html'

class EmailBlock(blocks.StructBlock):
        email = blocks.EmailBlock(classname="email")
        class Meta:
            template = 'header_footer/blocks/email.html'

class BusinessHourBlock(blocks.StaticBlock):
        def get_context(self, request):
            context = super().get_context(request)
            business_hour = OpenHour.objects.all().order_by('day_of_the_week')
            context['business_hour'] = business_hour
            return context
        class Meta:
            template = 'open_hours/business_hours.html'

@register_snippet
class FooterColumn(models.Model):
    footer_col_heading = 'Footer Column'
    footer_col = StreamField([
        ('heading', HeadingBlock(classname="full title")),
        ('table', TableBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('telephone', TelephoneBlock()),
        ('image', ImageChooserBlock()),
        ('table', TableBlock()),
        ('email', EmailBlock()),
        ('business_hours', BusinessHourBlock()),

    ], blank=True)
    class Meta:
        verbose_name = "First Footer Column"
    def __str__(self):
        return self.footer_col_heading

    panels = [
        StreamFieldPanel('footer_col'),
    ]
