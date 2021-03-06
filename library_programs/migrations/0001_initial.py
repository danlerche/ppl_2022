# Generated by Django 3.2.8 on 2022-05-20 17:42

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_range', models.CharField(blank=True, max_length=300, null=True)),
                ('color', wagtail_color_panel.fields.ColorField(blank=True, max_length=7, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=300, null=True)),
                ('color', wagtail_color_panel.fields.ColorField(blank=True, max_length=7, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeats', models.CharField(blank=True, choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly'), ('YEARLY', 'Yearly')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('time_from', models.TimeField(null=True)),
                ('time_to', models.TimeField(null=True)),
                ('description', wagtail.core.fields.RichTextField(blank=True, max_length=1500, null=True)),
                ('until', models.DateField(blank=True, null=True)),
                ('age_range', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_age', to='library_programs.eventage')),
                ('event_category', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_category', to='library_programs.eventcategory')),
                ('repeats', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_programs.occurrence', verbose_name='repeat')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
