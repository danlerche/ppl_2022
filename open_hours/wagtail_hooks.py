from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import (BranchInfo, OpenHour, ClosedDate, EnableMessageDisplay)

class EnableMessageDisplayAdmin(ModelAdmin):
    model = EnableMessageDisplay
    menu_label = 'Enable Messages'
    menu_icon = 'tick'
    list_display = ('enable_message_display',)

class BranchInfoAdmin(ModelAdmin):
    model = BranchInfo
    menu_label = 'Branch Info'
    menu_icon = 'home'

class OpenHoursAdmin(ModelAdmin):
    model = OpenHour
    menu_label = 'Open Hours'
    menu_icon = 'list-ul'
    list_display = ('day_of_the_week', 'time_from', 'time_to','open_closed' ,'branch_info')

class ClosedDatesAdmin(ModelAdmin):
    model = ClosedDate
    menu_label = 'Exception Dates'
    menu_icon = 'list-ul'
    list_display = ('closed_date_name', 'closed_date_from', 'closed_date_to', 'all_day', 'time_from', 'time_to', 'branch_info')

class OpenHoursGroup(ModelAdminGroup):
      menu_label = 'Open Hours'
      menu_icon = 'edit'
      menu_order = 225
      items = (EnableMessageDisplayAdmin,BranchInfoAdmin, OpenHoursAdmin, ClosedDatesAdmin)

modeladmin_register(OpenHoursGroup)
