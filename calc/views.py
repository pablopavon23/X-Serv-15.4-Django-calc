from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hola ' + request.method + '</h1>')

def adios(request, parametro):
    return HttpResponse('<h1>Adios ' + parametro + '</h1>')

def sumador(request, parametro):
    try:
        sumandos = parametro.split('+')
        sumando1 = sumandos[0]
        sumando2 = sumandos[1]
        suma = int(sumando1) + int(sumando2)
        return HttpResponse('<h1>Esto es una suma de ' + parametro + ', cuyo resultado es ' + str(suma) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Debes introducir una suma con url del tipo: IP:puerto/suma/sumando1+sumando2</h1>')

def restador(request, parametro):
    try:
        restandos = parametro.split('-')
        restando1 = restandos[0]
        restando2 = restandos[1]
        resta = int(restando1) - int(restando2)
        return HttpResponse('<h1>Esto es una suma de ' + parametro + ', cuyo resultado es ' + str(resta) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Debes introducir una resta con url del tipo: IP:puerto/resta/numero1-numero2</h1>')

def multiplicador(request, parametro):
    try:
        factores = parametro.split('*')
        factor1 = factores[0]
        factor2 = factores[1]
        multiplicacion = int(factor1) * int(factor2)
        return HttpResponse('<h1>Esto es una suma de ' + parametro + ', cuyo resultado es ' + str(multiplicacion) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Debes introducir una multiplicacion con url del tipo: IP:puerto/multi/factor1*factor</h1>')

def divisor(request, parametro):
    try:
        divisores = parametro.split('/')
        divisor1 = divisores[0]
        divisor2 = divisores[1]
        division = float(divisor1) / float(divisor2)
        return HttpResponse('<h1>Esto es una suma de ' + parametro + ', cuyo resultado es ' + str(division) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Debes introducir una division con url del tipo: IP:puerto/divison/divisor1/divisor2</h1>')

