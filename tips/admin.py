from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Recomendacion
# Register your models here.

#Resource
class RecomendacionResource(resources.ModelResource):
    class Meta:model = Recomendacion


# Register your models here.

class RecomendacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("titulo","descripcion")
    list_display = ("titulo","imagen","descripcion","creacion","actualizacion")
    resource_class=RecomendacionResource
    readonly_fields = ("creacion", "actualizacion")
    list_filter=("creacion","actualizacion")
   


admin.site.register(Recomendacion, RecomendacionAdmin)

