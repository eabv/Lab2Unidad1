# Importar librería Queue
from queue import Queue

class Grafo:
    """
    Clase de representación de un Grafo
    ...
    Atributos
    ----------
    num_Nodos : int
        Número de nodos del grafo
    dirigido : boolean
        Tipo de grafo dirigido o no dirigido

    Métodos
    -------
    Métodos Definidos

    __init__(numNodos, dirigido=True):
        Constructor de la clase Grafo, con todos sus atributos

    agregar_Arista(nodo1, nodo2, peso=1):
        Añade una arista a los nodos y agrega peso

    imprimir_ListaAdj():
        Impresión del gráfo

    busqueda_por_Amplitud(nodo_Inicio):
        Primera búsqueda por amplitud o anchura
    """
