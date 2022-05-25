# Generated by Django 3.2.8 on 2022-05-05 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('webform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='thank_you_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
    ]
