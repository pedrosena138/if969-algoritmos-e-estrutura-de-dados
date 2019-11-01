#-*- coding: utf-8 -*-

from grafo import Grafo 
#from dfs import busca_em_profundidade

def main():
    '''
    Grafo nao-direcionado nao-ponderado
    '''
    arestas = ((0,1),(1,2),(0,3), (2,3), (3,1))
    grafo = Grafo(arestas)
    print("Grafo nao-ponderado nao-direcionado")
    print(grafo)
    print("Busca em Profundidade:", grafo.busca_em_profundidade(0))
    print("Busca em Largura:", grafo.busca_em_largura(1))

    print("\nOs vertices (0) e (1) sao ligados?", grafo.ligados(0,1))
    print("Vertices adjacentes ao vertice (1):", grafo.adjacentes(1))
    print("Grau de entrada do vertice (2):", grafo.grau_entrada(2))
    print("Grau de saida do vertice (3):",grafo.grau_saida(3))

    print("\nInsercao do vertice (4)")
    grafo.inserir_vertice(4)
    print(grafo)
    
    print("Insercao da aresta (4,1)")
    grafo.inserir_aresta(4,1)
    print(grafo)

    print("Remoção da aresta (1,3)")
    grafo.remover_aresta(1,3)
    print(grafo)

    print("Remoção do vertice (2)")
    grafo.remover_vertice(2)
    print(grafo)

    print("Matriz de Adjacencia")
    grafo.imprimir_matriz()
    print(grafo)

if __name__ == "__main__":
    main()