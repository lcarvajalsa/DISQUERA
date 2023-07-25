# proyecto denominado trimestreV
from django.http import HttpResponse
import datetime
from django.template import Template, Context
#Request: Para realizar peticiones.
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP.
def bienvenida(request):# Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("Bienvenido o bienvenida a este curso de Django. =)")
def categoriaEdad(request, edad):
    if edad >=18:
        if edad >= 60:
            categoria="Tercera edad"
        else:
            categoria="Adultez"
    else:
        if edad <10:
            categoria="Infancia"
        else:
            categoria="Adolecencia"
    resultado="<h1>Categoria de edad: %s</h1>" %categoria
    return HttpResponse(resultado)    
def obtenerMomentoActual(request):
    #respuesta="<h1>Momento Actual: {0}</h1>".format(datetime.datetime.now())   
    respuesta="<h1>Momento Actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))          
    return HttpResponse(respuesta) 
def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body>
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)   
def miPrimeraPlantilla(request):
    #Abrimos el Documento que contiene a la plantilla:
    plantillaExterna = open("trimestreV/trimestreV/Plantillas/miPrimeraPlantilla.html") 
    #Cargar el documento externo que hemos abierto:
    template = Template(plantillaExterna.read())
    #Cerrar el documento externo que hemos abierto:
    plantillaExterna.close()
    #Crear un contexto:
    contexto = Context()
    #Renderizar el documento:
    documento = template.render(contenido)
    return HttpResponse(documento)
    