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
    # Constructor
    def __init__(self, num_Nodos, dirigido=True):
        """
        Método constructor de la clase Grafo, donde inicializa sus parámetros

        Parámetros
            ----------
            num_Nodos : int
                Número de nodos del grafo
            dirigido : boolean
                Tipo de grafo dirigido o no dirigido
        """
        # Define el número de nodos
        self.m_num_Nodos = num_Nodos
        # Define el rango del número de nodos
        self.m_Nodos = range(self.m_num_Nodos)

        # Tipo de grafo dirigido o no dirigido
        self.m_dirigido = dirigido

