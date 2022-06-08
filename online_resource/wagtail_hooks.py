from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import OnlineResourceCategory

class OnlineResourceCategoryAdmin(ModelAdmin):
    model = OnlineResourceCategory
    menu_label = 'Resource Categories' 
    menu_icon = 'list-ol' 
    list_display = ('name', 'category_image')


modeladmin_register(OnlineResourceCategoryAdmin)
