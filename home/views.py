from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render
from home.models import Auto
import random


def home(request):
    return HttpResponse("Bienvenido a mi INICIO")

def template1(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f"<h1>Mi template 1</h1>: {fecha} -- Hola {nombre} {apellido}")

def template2(request, nombre, apellido):
    template = loader.get_template("template2.html")
    
    datos = {
        "nombre": nombre,
        "apellido": apellido
    }
    
    template_render = template.render(datos)
    return HttpResponse(template_render)

def template3(request, nombre, apellido):
    datos = {
        "nombre": nombre,
        "apellido": apellido
    }
    return render(request, "template2.html", datos)

def probando(request):
    lista = list(range(500))
    datos = random.choices(lista, k=50)
    return render(request, "test_bucles.html", {"numeros": datos})

def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca, modelo=modelo)
    auto.save()
    return render(request, "auto_templates/creacion.html", {"marca":auto.marca, "modelo": auto.modelo})