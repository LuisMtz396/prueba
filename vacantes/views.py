from django.shortcuts import render
from vacantes.models import Vacante
# Create your views here.

def  vacantes(request):
    # QUE IMPORTE TODAS LAS VACANTES QUE HAYAMOS CONSTRUIDO
    vacantes = Vacante.objects.all()
    return render(request,"vacantes/vacantes.html",{'vacantes': vacantes})
