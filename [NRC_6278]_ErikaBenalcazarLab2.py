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

        # Representación de la lista de adyacencia
        # Para la implementación de la lista de adyacencia se usa un diccionario
        self.m_lista_adyacencia = {node: set() for node in self.m_Nodos}

    # Añande una arista al grafo
    def agregar_Arista(self, nodo1, nodo2, peso=1):
        '''
        Agrega una arista a los nodos del grafo, además añade el peso de cada 
        arista.

        Parámetros
        ----------
        nodo1 : int
            Entrada de dato tipo entero para el nodo1 
        nodo2 : int
            Entrada de dato tipo entero para el nodo2 
        peso : int
            Entrada de dato tipo entero para el 
        '''

        #En la lista de adyacencia toma el nodo 1 y agrega el nodo 2 y su peso.
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))

        # Agrega una arista a otro nodo cuando el grafo no sea dirigido
        if not self.m_dirigido:
            # Se agrega al nodo 2, el nodo 1 y su peso
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))

    # Imprime de manera representativa el grafo creado
    def imprimir_ListaAdj(self):
        # Realiza un recorrido con un for sobre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # Imprime cada nodo que se encuentra en la lista de adyacencia
            print("Nodo", llave, ": ", self.m_lista_adyacencia[llave])

    # Funcion de busqueda por amplitud o anchura
    def busqueda_por_Amplitud(self, nodo_Inicio):
        '''
        En esta búsqueda parte desde de un nodo inicial y luego recorre a otros nodos en función de sus nodos adyacentes.
        
        Parámetros
        ----------
        nodo_Inicio: int
            Nodo de inicio del grafo
        '''
        #Setea nos nodos visitados
        nodo_visitado = set()
        #Inicializa la cola del grafo
        cola = Queue()

        #Agrega a la cola el nodo Inicio
        cola.put(nodo_Inicio)
        #Agrega el nodo inicio como nodo visitado
        nodo_visitado.add(nodo_Inicio)
        #Realiza un bucle while para ver que no este vacía la cola
        while not cola.empty():
            # Pone a la cola el nodo Actual
            nodo_Actual = cola.get()
            # Imprime en nodo Actual
            print(nodo_Actual, end=" ")

            #Recorre la lista de adyacencia para ver todos los nodos adyacentes
            for (nodo_Siguiente, weight) in self.m_lista_adyacencia[nodo_Actual]:
                #Condición: verifica si el nodo ha sido visitado debe agregar a la cola
                if nodo_Siguiente not in nodo_visitado:
                    #Agrega a la cola el siguiente nodo
                    cola.put(nodo_Siguiente)
                    #Agrega el siguiente como nodo visitado
                    nodo_visitado.add(nodo_Siguiente)

#Main (Función principal de ejecución)
if __name__ == "__main__":
    #Instancia el objeto Grafo, agrega valores
     g = Grafo(6, dirigido = False)

    #Agrega las aristas del objeto grafo
    g.agregar_Arista(0, 1, 3)
    g.agregar_Arista(2, 2, 1)
    g.agregar_Arista(3, 2, 2)
    g.agregar_Arista(4, 3, 3)
    g.agregar_Arista(5, 0, 2)
    g.agregar_Arista(1, 3, 4)
    
    #Imprime la lista de adyacencia 
    g.imprimir_ListaAdj()

    print("Se muestra el recorrido por BFS"
          " (partiendo del vértice 0)")

    #Imprime la lista de colas visitadas
    g.busqueda_por_Amplitud(0)
    print()
    #Imprime la documentación del script
    help(Grafo)




