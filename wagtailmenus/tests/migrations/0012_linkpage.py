# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0011_auto_20170106_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='link to a custom URL')),
                ('url_append', models.CharField(blank=True, help_text="Use this to optionally append a #hash or querystring to the above page's URL.", max_length=255, verbose_name='append to URL')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='link to an internal page')),
                ('extra_classes', models.CharField(blank=True, help_text='Optionally specify additional css classes to be added to this page when it appears in menus as a menu item.', max_length=100, verbose_name='menu item css classes')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
