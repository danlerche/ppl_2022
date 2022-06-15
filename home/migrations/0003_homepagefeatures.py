# Generated by Django 3.2.8 on 2022-06-15 16:49

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('aspen_collection_spotlight_iframe', models.CharField(blank=True, help_text='see https://search.pentictonlibrary.ca/Admin/CollectionSpotlights for collection spotlight iframe tags', max_length=300, null=True)),
                ('home_page_features', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='homepage_feature', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
