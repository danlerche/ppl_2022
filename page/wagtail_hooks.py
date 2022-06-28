from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import PolicyCategory

class PolicyCategoryAdmin(ModelAdmin):
    model = PolicyCategory
    menu_label = 'Policy Categories'
    menu_icon = 'list-ol'

modeladmin_register(PolicyCategoryAdmin)
