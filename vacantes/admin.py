from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Vacante
# Register your models here.

#Resource
class VacanteResource(resources.ModelResource):
    class Meta:model = Vacante


# Register your models here.

class VacanteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("nombre_empresa","giro_empresarial")
    list_display = ("nombre_empresa","giro_empresarial","imagen","creacion","actualizacion")
    resource_class=VacanteResource
    readonly_fields = ("creacion", "actualizacion")
    list_filter=("giro_empresarial","creacion","actualizacion")
   


admin.site.register(Vacante, VacanteAdmin)

