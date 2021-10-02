from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):

    #nombre = "Juan"
    #apellido = "Diaz"
    p1 = Persona("Profesor Juan","Diaz")

    ahora=datetime.datetime.now()
    doc_externo=open("Proyecto1/plantilla/miplantilla.html")
    
    plt=Template(doc_externo.read())  
    doc_externo.close() 
    ctx =Context({"nombre_persona" : p1.nombre , "apellido_persona":p1.apellido, "momento_actual":ahora})
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
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)#esta forma no es recomendada 

    return HttpResponse(documento)