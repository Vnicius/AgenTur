import csv
from delayTime import DelayTime
from route import Route

class RoutesGenerator():
    '''
        Gera a matriz de rotas com as distâncias e o algoritmos de
        previsão, se possíveis
    '''
    def __init__(self, lista_pontos_ligados):
        self.lista_pontos_ligados = lista_pontos_ligados

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
                rota = Route()  
                rota.set_distancia(distancias[i][j])

                if [i, j] in self.lista_pontos_ligados \
                    or [j, i] in self.lista_pontos_ligados:

                    index = 0

                    try:
                        index = self.lista_pontos_ligados.index([i, j])
                    except ValueError:
                        index = self.lista_pontos_ligados.index([j, i])
                    
                    rota.set_delay_calculator(DelayTime(str(index + 1)))

                aux.append(rota)
            
            rotas.append(aux)

        return rotas 

if __name__ == "__main__":
    generator = RoutesGenerator([[0,1], [2,3]])
    rotas = generator.gerar_rotas()

    print(rotas[0][1].prever(5,13,5))