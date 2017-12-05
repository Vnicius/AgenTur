
from buscaheuristica.a_estrela import AEstrela
from buscaheuristica.vertice import Vertice
from buscaheuristica.aresta import Aresta
from routesGenerator import RoutesGenerator

VERTICES_CONT = 15
VELOCIDADE_MEDIA_ONIBUS = 60

def contruir_grafo(inicio, fim, dia, hora, fluxo, 
                    lista_pontos_adj, lista_pontos_turisticos, 
                    dict_rotas):

    generator = RoutesGenerator(lista_pontos_adj)
    matriz_rotas = generator.gerar_rotas()

    vertices = []

    for index in range(VERTICES_CONT):
        vertices.append(Vertice('E' + str(index + 1), 
                                matriz_rotas[index][fim - 1].distancia,
                                True if index in lista_pontos_turisticos else False))
    
    for i in range(VERTICES_CONT):
        for j in range(VERTICES_CONT):
            if [i, j] in lista_pontos_adj \
               or [j, i] in lista_pontos_adj:

                adj = vertices[j]
                rota_cor = ""
                adicional_trafego = VELOCIDADE_MEDIA_ONIBUS * (matriz_rotas[i][j].prever(dia, hora, fluxo)/60)

                if i in dict_rotas["vermelho"] \
                    and j in dict_rotas["vermelho"]:

                    rota_cor = "vermelho"

                elif i in dict_rotas["azul"] \
                     and j in dict_rotas["azul"]:
                    
                    rota_cor = "vermelho"

                elif i in dict_rotas["roxo"] \
                    and j in dict_rotas["roxo"]:
                    
                    rota_cor = "roxo"

                elif i in dict_rotas["rosa"] \
                    and j in dict_rotas["rosa"]:
                    
                    rota_cor = "rosa"

                vertices[i].add_aresta_adj(Aresta(vertices[j], matriz_rotas[i][j].distancia,
                                           rota_cor, adicional_trafego))

    return vertices

if __name__ == "__main__":
    import sys

    inicio = int(sys.argv[1])
    fim = int(sys.argv[2])
    prioriza_pt = int(sys.argv[3]) if len(sys.argv) == 4 else 50
    dia = 1
    hora = 14
    fluxo = 10

    lista_pontos_adj = [[0, 1], [1, 3], [3, 8], 
                        [8, 9], [9, 10], [10, 12], 
                        [12, 13], [13, 11], [11, 14], 
                        [14, 4], [4, 2], [2, 7], 
                        [6, 7], [6, 5], [5, 4], 
                        [3, 7], [11, 7], [7, 10]]

    lista_pontos_turisticos = [1, 6, 12, 13, 14]

    dict_rotas = {"vermelho" : [0, 1, 3, 7],
                  "azul" : [3, 8, 9, 10, 11, 12, 13],
                  "roxo" : [4, 6, 7, 11, 14],
                  "rosa" : [2, 4, 5, 6, 7]}

    vertices = contruir_grafo(inicio, fim, dia, hora, fluxo,
                              lista_pontos_adj, lista_pontos_turisticos, dict_rotas)
    
    caminho, custo = AEstrela(vertices, prioriza_pt).a_estrela(vertices[inicio - 1], vertices[fim - 1], 15)
    print('Menor Caminho: {}'.format(' -> '.join(caminho)))