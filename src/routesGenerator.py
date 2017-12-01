import csv
from delayTime import DelayTime
from route import Route

class RoutesGenerator():
    '''
        Gera a matriz de rotas com as distâncias e o algoritmos de
        previsão, se possíveis
    '''
    def __init__(self, lista_pontos_adj):
        self.lista_pontos_adj = lista_pontos_adj

    def __pegar_distancias(self):
        distancias = []
        with open("dataset/distancias.csv", newline="") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                distancias.append([float(el) for el in row])
        return distancias

    def gerar_rotas(self):
        distancias = self.__pegar_distancias()

        rotas = []

        for i in range(15):
            aux = []
            for j in range(15):
                rota = Route(distancias[i][j])  

                if [i, j] in self.lista_pontos_adj \
                    or [j, i] in self.lista_pontos_adj:

                    index = 0

                    try:
                        index = self.lista_pontos_adj.index([i, j])
                    except ValueError:
                        index = self.lista_pontos_adj.index([j, i])
                    
                    rota.set_delay_calculator(DelayTime(str(index)))

                aux.append(rota)
            
            rotas.append(aux)

        return rotas 

if __name__ == "__main__":
    lista_pontos_adj = [[0, 1], [1, 3], [3, 8], 
                        [8, 9], [9, 10], [10, 12], 
                        [12, 13], [13, 11], [11, 14], 
                        [14, 4], [4, 2], [2, 7], 
                        [6, 7], [6, 5], [5, 4], 
                        [3, 7], [11, 7], [7, 10]]
    
    print(len(lista_pontos_adj))
    lista_rotas = [[0, 1, 3, 7],
                   [3, 8, 9, 10, 11, 12, 13],
                   [4, 6, 7, 11, 14],
                   [2, 4, 5, 6, 7]]

    generator = RoutesGenerator(lista_pontos_adj)
    matriz_rotas = generator.gerar_rotas()
    
    print(matriz_rotas)

    if matriz_rotas[0][1].delay_calculator:
        print(matriz_rotas[0][1].prever(5,13,5))