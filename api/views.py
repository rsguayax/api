'''
Esta clase SubarregloSerializer en función de los parámetros de entrada del método, estructura los atributos requeridos: target y array'''
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

class SubarregloSerializer(serializers.Serializer):
    #aquí he colocado los nombres de los campos del json de entrada
    target = serializers.IntegerField()
    array = serializers.ListField(child=serializers.IntegerField())

#método para generar el subarreglo máximo
def generar_sub_arreglo(n_objetivo, arreglo):
    tam = len(arreglo)
    max_len = 0  # almaceno la longitud máxima del subarreglo
    salida = []  # mejor respuesta, subarreglo de longitud máxima
    
    # Recorrido general de cada posición de: arreglo
    for i in range(tam):
        suma = 0 #acumulador de sumas
        tam_actual = 0
        #recorrido interno por cada posición del arreglo, aquí se van descartando las posiciones ya recorridas
        for j in range(i, tam):
            suma += arreglo[j]
            tam_actual+=1
            #preguntamos si la suma obtenida es igual al objetivo buscado
            if suma == n_objetivo:
                if tam_actual > max_len:#si el tamaño actual del arreglo es mayor, entonces actualizamos el subarreglo máximo y longitud en max_len
                    max_len = tam_actual
                    salida = arreglo[i:j+1]#cortamos el arreglo desde la posición que se encuentre i, hasta j+1
    
    return salida #retorno el subarreglo máximo, en caso de que el arreglo no tenga elementos o no se encontró el número objetivo, será []

'''En esta clase he colocado el método post que se invocará cuando se coloquen el json de entrada, se devolverá el json de salida'''
class SubarregloView(APIView):
    def post(self, request):
        serializer = SubarregloSerializer(data=request.data)
        #validamos si es correcto el json de entrada
        if serializer.is_valid():
            n_objetivo = serializer.validated_data['target']
            arreglo = serializer.validated_data['array']
            resultado = generar_sub_arreglo( n_objetivo, arreglo)
            return Response({'subarray': resultado}, status=status.HTTP_200_OK)#retorno json de salida
        else:
            return Response({'mensaje:':'json de entrada incorrecto'},status.HTTP_400_BAD_REQUEST)
