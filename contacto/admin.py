from django.contrib import admin
from .models import Registro
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Resource
class RegistroResource(resources.ModelResource):
    class Meta:model = Registro
    # Register your models here.
class RegistroAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("nombre","correo","mensaje")
    list_display=("nombre","correo","mensaje")
    resource_class=RegistroResource
   # list_filter=("nombre","correo",)



admin.site.register(Registro,RegistroAdmin)