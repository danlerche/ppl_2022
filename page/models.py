from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.core.blocks import DateBlock, DateTimeBlock, URLBlock, EmailBlock, TimeBlock, StreamBlock, ChoiceBlock
from wagtail.core.blocks import DateTimeBlock, TimeBlock, BlockQuoteBlock, PageChooserBlock, ListBlock, BooleanBlock, TextBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.search import index
from wagtailgeowidget.blocks import GeoBlock, GeoAddressBlock
from wagtailgeowidget.edit_handlers import GeoPanel
from wagtail.embeds.oembed_providers import youtube, vimeo
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from unidecode import unidecode
from django.template import defaultfilters
from library_programs.models import EventCategory


class groupPage(Page):
    pass

class AllPurposePage(Page):
# tutorial to add web forms to the pages. Not a stream for but who cares https://stackoverflow.com/questions/48636619/wagtail-feedback-form-in-homepage
    #try:
    #    event_category_choice = EventCategory.objects.values_list('id', 'category_name')
    #except:
    #    event_category_choice = []
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('BlockQuoteBlock', BlockQuoteBlock(template='page/blocks/block_quote.html')),
        ('text_only_table', TableBlock()),
        ('richtext_table', TypedTableBlock([
            ('rich_text', blocks.RichTextBlock()),
        ])),
        ('URLBlock', URLBlock()),
        ('EmailBlock', EmailBlock()),
        ('all_upcoming_events', BooleanBlock(required=False, help_text="If checked, all upcoming events will display", icon='tasks')),
        #('calendar_upcoming', ChoiceBlock(choices=calendar_choice, icon='date')),
        ('DateBlock', DateBlock()),
        ('TimeBlock', TimeBlock()),
        ('DateTimeBlock', DateBlock()),
        ('PageChooserBlock', PageChooserBlock()),
        ('DocumentChooserBlock', DocumentChooserBlock()),
        ('PhoneNumberBlock', TextBlock()),
        ('EmbedBlock', EmbedBlock()),
        ('ppl_map', BooleanBlock(required=False, help_text="If checked, a Google map will appear", icon='user')),
        ('map', blocks.StructBlock([
            ('address', GeoAddressBlock(required=True)),
            ('map', GeoBlock(address_field='address')),
        ], template='page/blocks/map.html', icon='user')),
        ('show_business_hours', BooleanBlock(required=False, help_text="If checked, the library hours will display on the page", icon='user')),
        ('show_next_closure', BooleanBlock(required=False, help_text="If checked, the next library closure will display", icon='user')),
        ('show_all_closures', BooleanBlock(required=False, help_text="If checked, all upcoming library closures will be shown", icon='user')),
        ('bookClub', blocks.StructBlock([
            ('book_club_name', blocks.CharBlock()),
            ('book_club_day_of_the_week', blocks.TextBlock()),
            ('book_club_PDF', DocumentChooserBlock(required=False)),
            ('book_club_time', blocks.TimeBlock()),
            ('books', blocks.StreamBlock(
                [
                    ('book', blocks.StructBlock([
                        ('book_name', blocks.CharBlock()),
                        ('author_name', blocks.CharBlock()),
                        ('reading_date', blocks.DateBlock()),
                        ('book_description', blocks.RichTextBlock()),
                        ('book_cover', ImageChooserBlock(required=False)),
                    ],template='page/blocks/books.html'),),
                ]
            )),
            ], template='page/blocks/book_club.html', icon='openquote')),
        ('columnBlock', blocks.StructBlock([
            ('column', blocks.StreamBlock([
                ('richtext', blocks.RichTextBlock()),
                ('block_quote', BlockQuoteBlock(template='page/blocks/block_quote.html')),
                ('image', ImageChooserBlock(required=False)),
            ]))
        ],template='page/blocks/column.html', icon='table')),
        ('accordion', blocks.StructBlock([
            ('accordion_name', blocks.CharBlock()),
            ('only_one_open', blocks.BooleanBlock(required=False, default=True, help_text="Automatically close all other accordions while another is open")),
            ('accordion_body', blocks.StreamBlock(
                [
                    ('accordion_items', blocks.StructBlock([
                        ('accordion_item_title', blocks.CharBlock()),
                        ('accordion_description', blocks.RichTextBlock()),
                        ('show_by_default', blocks.BooleanBlock(required=False, help_text="Display accordion as open by default")),
                    ]),),
                ]
            )),
            ], template='page/blocks/accordion.html', icon='collapse-down')),

    ], blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]
