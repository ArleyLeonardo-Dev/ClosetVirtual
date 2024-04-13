from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
import random


#Base de datos
class ZapatosView(viewsets.ModelViewSet):
    queryset = Zapatos.objects.all()
    serializer_class = ZapatosSerilizer

class PantalonesFaldasView(viewsets.ModelViewSet):
    queryset = PantalonesFaldas.objects.all()
    serializer_class = PantalonesFaldasSerilizer

class CamisasView(viewsets.ModelViewSet):
    queryset = Camisas.objects.all()
    serializer_class = CamisasSerilizer

class VestidosView(viewsets.ModelViewSet):
    queryset = Vestidos.objects.all()
    serializer_class = VestidosSerilizer

class CombinacionesView(APIView):

    def get(self, request):

        zapatos = []#Lista vacia donde entraran todos los objetos de la base de datos
        zapatosquery = Zapatos.objects.all()#Variable que guardara el query de la base de datos
        for x in zapatosquery:
            zapatos.append(Zapatos.objects.get(pk = x.id))#En este ciclo for se añadira cada objeto a la lista
        NumZ = len(zapatos)#Se Calcula cuantos elementos tiene la lista de objetos
        Zapato = zapatos[random.randint(0,NumZ - 1)]#Selecciona un objeto aleatorio de la lista

        combo = random.randint(1,2)#Selecciona entre dos modos "Vestidos y ropa normal"

        if combo == 1:#Modo 1

            pantalones = []
            camisas = []

            pantalonesquery = PantalonesFaldas.objects.all()
            camisasquery = Camisas.objects.all()

            for x in pantalonesquery:
                pantalones.append(PantalonesFaldas.objects.get(pk = x.id))
            
            for x in camisasquery:
                camisas.append(Camisas.objects.get(pk = x.id))

            NumP = len(pantalones)
            NumC = len(camisas)

            Pantalon = pantalones[random.randint(0, NumP - 1)]
            Camisa = camisas[random.randint(0, NumC - 1)]

            #Lista con los 3 objetos random de la base de datos
            lista = [Zapato, Pantalon, Camisa]
            listaN = ["Zapatos", "PantalonesFaldas", "Camisas"]
            
            combinacion={}
            
            #Se inserta en la lista combinacion el nombre y el color de cada elemento de la lista
            for x in range(3):
                combinacion[listaN[x]] = str(lista[x].nombre + " " + lista[x].color)

            return Response(combinacion, status.HTTP_200_OK)
        

        if combo == 2:#Modo 2

            vestidos = []

            vestidosquery = Vestidos.objects.all()

            for x in vestidosquery:
                vestidos.append(Vestidos.objects.get(pk = x.id))

            NumV = len(vestidos)

            Vestido = vestidos[random.randint(0, NumV - 1)]

            lista = [Zapato, Vestido]
            listaN = ["Zapatos", "Vestidos"]

            combinacion = {}

            for x in range(2):
                combinacion[listaN[x]]= str(lista[x].nombre + " " + lista[x].color)
            
            return Response(combinacion, status.HTTP_200_OK)
        
    def post(self, request):

        datos = CombinacionesSerilizer(data = request.data)
        
        if datos.is_valid():
            datos.save()
            mensaje ={"Mensaje":"Combinacion Guardada"}
            return Response(mensaje, status.HTTP_200_OK)
        return Response(datos.errors, status.HTTP_400_BAD_REQUEST)
    


class DetalleCombinacionesView(APIView):

    def get(self, request, pk):
        
        Combinacion = Combinaciones.objects.get(pk = pk)
        
        if Combinacion.Vestidos == None:
            data = {"Zapatos": Combinacion.Zapatos, "PantalonesFaldas": Combinacion.PantalonesFaldas, "Camisas":Combinacion.Camisas}
        else:
            data = {"Zapatos": Combinacion.Zapatos, "Vestidos":Combinacion.Vestidos}

        return Response(data, status.HTTP_200_OK)

    def delete(self, request, pk):
        combinacion = Combinaciones.objects.get(pk = pk)
        combinacion.delete()
        combinacion.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

        