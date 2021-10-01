from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    #return HttpResponse("Hola alumnos esta es nuestra primera pagina con Django")
    doc_externo=open("Proyecto1/plantilla/miplantilla.html")
    
    plt=Template(doc_externo.read())  
    doc_externo.close() 
    ctx =Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de django")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    la fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

#def calculaEdad(request,agno):
def calculaEdad(request,edad,agno):
    #edadActual=18
    periodo=agno-2021
    #edadFutura=edadActual+periodo
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(documento)