from django.shortcuts import render
from .models import Oportunidades
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class OportunidadesAbm(APIView):
    def get(self,request):
        aceptados= Oportunidades.objects.filter(aceptados=True)
        CantAceptados= Oportunidades.objects.filter(aceptados=True).count()
        rechazados= Oportunidades.objects.filter(aceptados=False).count()
        total = Oportunidades.objects.all().count()
        empezoConNo= Oportunidades.objects.filter(empezoConNo=True).count()
        if total==0:
            total=1

        porcentajeAceptado= (CantAceptados/total)*100
        porcentajeRechazaddo= (rechazados/total)*100
        
        cantidadNumerosVendidos=0
        for aceptado in aceptados:
            cantidadNumerosVendidos += aceptado.cantidad  

        montoVendido= cantidadNumerosVendidos *2500
        data={
                'TotalOportunidades': total or 0,
                'OportunidadesAceptadas': CantAceptados or 0,
                'OportunidadesRechazadas': rechazados or 0,
                'CantidadNumerosVendidos': cantidadNumerosVendidos or 0,
                'montoVendido': montoVendido or 0,
                'PorcentajeAceptados': porcentajeAceptado or 0.0,
                'PorcentajeRechazados': porcentajeRechazaddo or 0.0,
                'empezaronConNo': empezoConNo or 0,
              }
        return Response({'mensaje': data})
    
    def post (self, request):

        data= request.data

        if 'aceptado' not in data:
            return Response({'error': 'falta el estado de aceptado'}, status=400)
        
        aceptado= data.get('aceptado')

        if aceptado == True:
            cantidad= data.get('cantidad') or 1
            empezoConNo= data.get('empezoConNo') or False

            oportunidad= Oportunidades.objects.create(aceptados=aceptado, cantidad=cantidad, empezoConNo=empezoConNo)
        else:
            oportunidad= Oportunidades.objects.create(aceptados=aceptado)
        
        return Response({'Mensaje':'Oportunidad creada con exito'}, status=200)