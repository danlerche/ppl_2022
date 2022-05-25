# Generated by Django 3.1.7 on 2021-03-30 22:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(blank=True, max_length=200, null=True)),
                ('street_number', models.SmallIntegerField(blank=True, null=True)),
                ('street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('province_state', models.CharField(blank=True, max_length=2, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=7, null=True)),
                ('telephone', models.CharField(blank=True, max_length=14, null=True)),
                ('closed_holiday_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('hours_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
        ),
        migrations.CreateModel(
            name='EnableMessageDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_message_display', models.BooleanField(default=1, help_text='uncheck to hide the open and closed hours display')),
            ],
        ),
        migrations.CreateModel(
            name='OpenHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_closed', models.BooleanField(choices=[(1, 'Open'), (0, 'Closed')], default=1)),
                ('day_of_the_week', models.SmallIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('time_from', models.TimeField(blank=True, null=True)),
                ('time_to', models.TimeField(blank=True, null=True)),
                ('branch_info', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='open_hours.branchinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ClosedDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed_date_name', models.TextField(default='holiday')),
                ('closed_date_from', models.DateField(default=datetime.date.today)),
                ('closed_date_to', models.DateField(default=datetime.date.today)),
                ('all_day', models.BooleanField(default=True, help_text='Default is checked. uncheck to have special holiday hours')),
                ('time_from', models.TimeField(blank=True, help_text='only takes effect if All Day is unchecked', null=True)),
                ('time_to', models.TimeField(blank=True, help_text='only takes effect if All Day is unchecked', null=True)),
                ('branch_info', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='open_hours.branchinfo')),
            ],
        ),
    ]
