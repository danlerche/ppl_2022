from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey

class HomePage(Page):

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel('homepage_feature', label="homepage Feature"),
                InlinePanel('aspen_carousel', label="Aspen Carousel"),
            ],

            heading = "Homepage Features ",
            classname = "collapisble collapse"
            ),
        ]

class HomePageFeatures(Orderable):
    home_page_features = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='homepage_feature')
    home_page_feature_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    home_page_feature_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+')
    home_page_feature_doc = models.ForeignKey('wagtaildocs.Document',null=True,blank=True,on_delete=models.SET_NULL,related_name='+', verbose_name="Link to a document instead of a page or external url. This will only work if no internal page, or external link is selected",)
    home_page_feature_text = models.CharField(blank=True, max_length=300, verbose_name="Overrides the title of the page")

    content_panels = Page.content_panels + [
        FieldPanel('home_page_feature_page'),
        FieldPanel('home_page_feature_image'),
        FieldPanel('home_page_feature_text'),
        FieldPanel('home_page_feature_doc'),
        FieldPanel('aspen_collection_spotlight_id'),
     ]

class HomePageAspenCarousel(Orderable):
    aspen_carousels = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='aspen_carousel')
    aspen_collection_spotlight_iframe = models.CharField(null=True, blank=True, max_length=300, help_text="see https://search.pentictonlibrary.ca/Admin/CollectionSpotlights for collection spotlight iframe tags")

    content_panels = Page.content_panels + [
        FieldPanel('aspen_collection_spotlight_id'),
     ]
