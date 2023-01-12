from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Egresado


# Register your models here.

#Resource
class EgresadoResource(resources.ModelResource):
    class Meta:model = Egresado  

class EgresadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("nombre","apellido_paterno","apellido_materno","edad","correo_institucional","telefono","generacion","carrera","posgrado","tipo_posgrado")
    list_display= ("nombre","apellido_paterno","apellido_materno","edad","correo_institucional","generacion","carrera","posgrado","tipo_posgrado","telefono","cv",)
    readonly_fields = ('creacion','actualizacion')
    list_filter=("carrera","posgrado","creacion","actualizacion")
    



admin.site.register(Egresado,EgresadoAdmin)