from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey

class HomePage(Page):

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel('homepage_feature', label="homepage Feature"),
            ],

            heading = "Homepage Features ",
            classname = "collapisble collapse"
            ),
        ]

class HomePageFeatures(Orderable):
    home_page_features = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='homepage_feature')
    aspen_collection_spotlight_iframe = models.CharField(null=True, blank=True, max_length=300, help_text="see https://search.pentictonlibrary.ca/Admin/CollectionSpotlights for collection spotlight iframe tags")

    content_panels = Page.content_panels + [
        FieldPanel('aspen_collection_spotlight_id'),
     ]
