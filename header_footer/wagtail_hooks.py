from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import (
    Logo, Alert, FooterColumn)

class LogoAdmin(ModelAdmin):
    model = Logo
    menu_label = 'Logo' 
    menu_icon = 'image / picture' 

class AlertAdmin(ModelAdmin):
    model = Alert
    menu_label = 'Alert' 
    menu_icon = 'pick' 
    list_display = ('enable_alert', 'alert_text', 'alert_colour')

class FooterColumnAdmin(ModelAdmin):
    model = FooterColumn
    menu_label = 'Footer Column 1'  
    menu_icon = 'doc-full-inverse'  
    list_display = ('footer_col_heading', 'footer_col')

class HeaderFooterGroup(ModelAdminGroup):
    menu_label = 'Header & Footer'
    menu_icon = 'edit'
    menu_order = 200  
    items = (LogoAdmin, AlertAdmin, FooterColumnAdmin)

modeladmin_register(HeaderFooterGroup)
