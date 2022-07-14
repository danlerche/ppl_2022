from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from django import forms
from django.shortcuts import render

@register_snippet
class OnlineResourceCategory(models.Model):
    name = models.CharField(max_length=255)
    category_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,related_name='+')

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('category_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'online resource categories'


class OnlineResourceIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        online_resource_pages = self.get_children().live()
        categories = OnlineResourceCategory.objects.all()
        context['online_resource_pages'] = online_resource_pages
        context['categories'] = categories
        return context


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class OnlineResourcePage(Page):
    online_resource_url = models.CharField(max_length=400, blank=True)
    online_resource_description = RichTextField(blank=True)
    resource_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL,related_name='+')
    categories = ParentalManyToManyField('online_resource.OnlineResourceCategory', blank=True)
    featured = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('online_resource_url'),
        FieldPanel('online_resource_description'),
        FieldPanel('resource_image'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('featured'),
    ]
