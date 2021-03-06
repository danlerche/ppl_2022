# Generated by Django 3.0.8 on 2020-11-26 03:53

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0004_auto_20201125_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footercolumn',
            name='footer_col',
            field=wagtail.core.fields.StreamField([('table', wagtail.contrib.table_block.blocks.TableBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('telephone', wagtail.core.blocks.StructBlock([('telephone', wagtail.core.blocks.CharBlock(classname='telephone'))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('email', wagtail.core.blocks.StructBlock([('email', wagtail.core.blocks.EmailBlock(classname='email'))])), ('business_hours', wagtail.snippets.blocks.SnippetChooserBlock(icon='list-ol', target_model='open_hours.OpenHour', template='open_hours/business_hours.html'))], blank=True),
        ),
    ]
