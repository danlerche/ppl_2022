# Generated by Django 3.0.8 on 2020-11-26 04:00

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0005_auto_20201125_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footercolumn',
            name='footer_col',
            field=wagtail.core.fields.StreamField([('table', wagtail.contrib.table_block.blocks.TableBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('telephone', wagtail.core.blocks.StructBlock([('telephone', wagtail.core.blocks.CharBlock(classname='telephone'))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('email', wagtail.core.blocks.StructBlock([('email', wagtail.core.blocks.EmailBlock(classname='email'))])), ('show_business_hours', wagtail.core.blocks.BooleanBlock(help_text='If checked, the library hours will display on the page', icon='user', required=False)), ('show_next_closure', wagtail.core.blocks.BooleanBlock(help_text='If checked, the next library closure will display', icon='user', required=False)), ('show_all_closures', wagtail.core.blocks.BooleanBlock(help_text='If checked, all upcoming library closures will be shown', icon='user', required=False))], blank=True),
        ),
    ]