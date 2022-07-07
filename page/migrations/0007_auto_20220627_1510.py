# Generated by Django 3.2.8 on 2022-06-27 22:10

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.contrib.typed_table_block.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailgeowidget.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('page', '0006_alter_allpurposepage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_category', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Policy categories',
            },
        ),
        migrations.CreateModel(
            name='PolicyIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('additional_text', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='allpurposepage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('BlockQuoteBlock', wagtail.blocks.BlockQuoteBlock(template='page/blocks/block_quote.html')), ('text_only_table', wagtail.contrib.table_block.blocks.TableBlock()), ('richtext_table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('rich_text', wagtail.blocks.RichTextBlock())])), ('URLBlock', wagtail.blocks.URLBlock()), ('EmailBlock', wagtail.blocks.EmailBlock()), ('all_upcoming_events', wagtail.blocks.BooleanBlock(help_text='If checked, all upcoming events will display', icon='tasks', required=False)), ('DateBlock', wagtail.blocks.DateBlock()), ('TimeBlock', wagtail.blocks.TimeBlock()), ('DateTimeBlock', wagtail.blocks.DateBlock()), ('PageChooserBlock', wagtail.blocks.PageChooserBlock()), ('DocumentChooserBlock', wagtail.documents.blocks.DocumentChooserBlock()), ('IframeBlock', wagtail.blocks.RawHTMLBlock(help_text='See https://search.pentictonlibrary.ca/Admin/CollectionSpotlights for info about using the iframe tag to embed Aspen Collection Spotlights.')), ('PhoneNumberBlock', wagtail.blocks.TextBlock()), ('EmbedBlock', wagtail.embeds.blocks.EmbedBlock()), ('ppl_map', wagtail.blocks.BooleanBlock(help_text='If checked, a Google map will appear', icon='user', reqonline_resourceuired=False)), ('map', wagtail.blocks.StructBlock([('address', wagtailgeowidget.blocks.GeoAddressBlock(required=True)), ('map', wagtailgeowidget.blocks.GeoBlock(address_field='address'))], icon='user', template='page/blocks/map.html')), ('show_business_hours', wagtail.blocks.BooleanBlock(help_text='If checked, the library hours will display on the page', icon='user', required=False)), ('show_next_closure', wagtail.blocks.BooleanBlock(help_text='If checked, the next library closure will display', icon='user', required=False)), ('show_all_closures', wagtail.blocks.BooleanBlock(help_text='If checked, all upcoming library closures will be shown', icon='user', required=False)), ('bookClub', wagtail.blocks.StructBlock([('book_club_name', wagtail.blocks.CharBlock()), ('book_club_day_of_the_week', wagtail.blocks.TextBlock()), ('book_club_PDF', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('book_club_time', wagtail.blocks.TimeBlock()), ('books', wagtail.blocks.StreamBlock([('book', wagtail.blocks.StructBlock([('book_name', wagtail.blocks.CharBlock()), ('author_name', wagtail.blocks.CharBlock()), ('reading_date', wagtail.blocks.DateBlock()), ('book_description', wagtail.blocks.RichTextBlock()), ('book_cover', wagtail.images.blocks.ImageChooserBlock(required=False))], template='page/blocks/books.html'))]))], icon='openquote', template='page/blocks/book_club.html')), ('columnBlock', wagtail.blocks.StructBlock([('column', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('block_quote', wagtail.blocks.BlockQuoteBlock(template='page/blocks/block_quote.html')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], icon='table', template='page/blocks/column.html')), ('accordion', wagtail.blocks.StructBlock([('accordion_name', wagtail.blocks.CharBlock()), ('only_one_open', wagtail.blocks.BooleanBlock(default=True, help_text='Automatically close all other accordions while another is open', required=False)), ('accordion_body', wagtail.blocks.StreamBlock([('accordion_items', wagtail.blocks.StructBlock([('accordion_item_title', wagtail.blocks.CharBlock()), ('accordion_description', wagtail.blocks.RichTextBlock()), ('show_by_default', wagtail.blocks.BooleanBlock(help_text='Display accordion as open by default', required=False))]))]))], icon='collapse-down', template='page/blocks/accordion.html'))], blank=True, use_json_field=None),
        ),
        migrations.AddField(
            model_name='allpurposepage',
            name='policy_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pol_cat', to='page.policycategory'),
        ),
    ]