#!/usr/bin/python3
# -*- coding:utf-8 -*-
import heapq
from collections import defaultdict # lista de dicionarios

class No():
  def __init__(self, chave, h_de_n):
    '''
    h_de_n = distancia de n ate o destino final
    '''
    self.chave = chave
    self.h_de_n = h_de_n
  
  def __repr__(self):
    return 'Nó {} / h(n) = {}'.format(self.chave, self.h_de_n)

class Aresta():
  '''
  recebe objeto No origem e destino, 
  e distancia entre eles
  '''
  def __init__(self, no_origem, no_destino, distancia):
    self.no_origem = no_origem
    self.no_destino = no_destino
    self.distancia = distancia
  
  def __repr__(self):
    return 'Aresta {} -> {} com distância {}'.format(self.no_origem, self.no_destino, self.distancia)

class FilaDePrioridade:
    '''
    Fila de prioridade pelo menor f(n) - Heap Minimo
    '''
    def __init__(self):
        self._fila = []
        self._indice = 0

    def insere(self, item, prioridade):
        heapq.heappush(self._fila, (prioridade, self._indice, item))
        self._indice += 1

    def remove(self):
        return heapq.heappop(self._fila)[-1]

    def estaVazio(self):
        return len(self._fila) == 0

class Grafo():
  def __init__(self):
    self.nos = []
    self.arestas = []
    self.caminho = []
    self.sucessores = defaultdict(list) # cria lista de dicionario
    self.caminho = [] # caminho resultado

  def existeAresta(self, aresta):
    for a in self.arestas:
      if a.no_origem.chave == aresta.no_origem.chave and \
          a.no_destino == aresta.no_destino and \
            a.distancia == aresta.distancia:
            return True
      return False
  
  def adicionaAresta(self, aresta):
    if not self.existeAresta(aresta):
      # adicionar
      self.nos.append(aresta.no_origem)
      self.nos.append(aresta.no_destino)
      self.arestas.append(aresta) # adiciona aresta
      '''
      sucessores: Lista de dicionarios contendo 2-Tupla
          2-Tupla
            No origem, distancia entre origem e destino
      '''
      self.sucessores[aresta.no_origem.chave].append((aresta.no_destino, aresta.distancia))
    else:
      raise ValueError('Erro: {} já existe e nao foi adicionada!'.format(aresta))

  def aEstrela(self, no_inicial, no_final):
    
    if not self.arestas:
      raise ValueError('Erro: Grafo vazio!')
    
    if not no_inicial in self.nos:
      raise ValueError('Erro: No inicial nao foi adicionado!')
    
    if not no_final in self.nos:
      raise ValueError('Erro: No final nao foi adicionado!')
    
    if no_inicial == no_final:
      return 0
    
    # Cria Fila de Prioridade
    fila = FilaDePrioridade()

    '''
    Dicionario
      distancia_ate_n: Representa a distancia do no inicial
                      ate o no N.
      antecessor: No antecessor a N.
    '''
    distancia_ate_n, antecessor = {}, {}
    # inicializa para todos os nos
    for no in self.nos:
      distancia_ate_n[no.chave] = None
      antecessor[no.chave] = None

    # No inicial
    # Como eh o no inicial, distancia ate ele eh zero
    distancia_ate_n[no_inicial.chave] = 0
    g_de_n = 0
    h_de_n = no_inicial.h_de_n
    f_de_n = g_de_n + h_de_n
    
    # Insiro primeiro item na fila de prioridade
    '''
    Parametros: 
      3-Tupla
        no_atual
        g_de_n referente ao no_atual
        h_de_n referente ao no_atual
      Prioridade
        f_de_n referente ao no_atual
    '''

    fila.insere( (no_inicial, g_de_n, h_de_n), f_de_n )
    custo_total = None

    while True:
      # Retira elemento de menor f(n) da Fila de Prioridade
      #print(fila._fila)
      no_atual, g_de_n, h_de_n = fila.remove() # descompacta tupla

      # Recupera todos os sucessores do no_atual
      sucessores = self.sucessores[no_atual.chave]

      # Para cada sucessor, calcula f(n)
      for sucessor in sucessores:
        # sucessor = (no_destino, distancia)        
        no_destino, distancia = sucessor
        '''
          Para o sucessor atual temos que:
          g(sucessor) = g(antecessor) + distancia entre eles
        '''
        novo_g_de_n = g_de_n + distancia        
        # h(n) distancia ate o destino final (consultar tabela)
        h_de_n = no_destino.h_de_n
        # f(n) = g(n) + h(n)
        f_de_n = novo_g_de_n + h_de_n
        fila.insere( (no_destino, novo_g_de_n, h_de_n), f_de_n )

        '''
        Verifica e atualiza distancia_ate_n
          Caso seja um no nao conhecido:
            atribui distancia ate N representado por novo_g_de_n
            atribui seu antecessor, no caso, no_atual
          Caso contrario:
            Verifica se a nova distancia ate N (nova rota) eh maior que a ja calculada:
              Se sim, 
                mantem-se os valores de distancia e antecessor
              Caso contrario, 
                Atuliza a distancia ate N e o seu novo antecessor
        '''
        if distancia_ate_n[no_destino.chave]:
          if distancia_ate_n[no_destino.chave] > novo_g_de_n:
            distancia_ate_n[no_destino.chave] = novo_g_de_n
            antecessor[no_destino.chave] = no_atual.chave
        else:
          distancia_ate_n[no_destino.chave] = novo_g_de_n
          antecessor[no_destino.chave] = no_atual.chave

        '''
        Verifica se o no destino eh o no final
          Caso sim, Verifica se nao houve regresso (chegou no fim, mas voltou por outra rota)
            Caso nao, 
              Atribui o custo total, representado pelo f(n) do no final
            Caso sim, 
              Atualiza o novo custo total, sse ele o novo for menor que o antigo custo
        '''
        if no_destino.chave == no_final.chave:
          if not custo_total:
            custo_total = f_de_n
          elif f_de_n < custo_total:
            custo_total = f_de_n
      # for
      
      if fila.estaVazio():
        no = no_final.chave
        while no:
          self.caminho.append(no)
          no = antecessor[no]
        self.caminho.reverse()        
        return (custo_total, self.caminho)
    # while


if __name__ == '__main__':
  # noS = No('S', 3)
  # noA = No('A', 2)
  # noB = No('B', 1)
  # noG = No('G', 0)
  # grafo = Grafo()
  # grafo.adicionaAresta(Aresta(noS, noA, 2))
  # grafo.adicionaAresta(Aresta(noS, noB, 2))
  # grafo.adicionaAresta(Aresta(noA, noG, 2))
  # grafo.adicionaAresta(Aresta(noB, noG, 3))

  # custo, caminho = grafo.aEstrela(noS, noG)
  # print('Caminho: {}\nCusto Total: {}'.format(' -> '.join(caminho), custo))

  grafo = Grafo()
  noE1 = No('E1', 30)
  noE2 = No('E2', 23)
  noE3 = No('E3', 21)
  noE4 = No('E4', 21)
  noE5 = No('E5', 27)
  noE6 = No('E6', 30)
  noE7 = No('E7', 28)
  noE8 = No('E8', 7)
  noE9 = No('E9', 12)
  noE10 = No('E10', 27)
  noE11 = No('E11', 15)
  noE12 = No('E12', 0)
  noE13 = No('E13', 31)
  noE14 = No('E14', 37)

  grafo.adicionaAresta(Aresta(noE1, noE2, 11))
  
  # grafo.adicionaAresta(Aresta(noE2, noE1, 11))
  grafo.adicionaAresta(Aresta(noE2, noE3, 9))
  grafo.adicionaAresta(Aresta(noE2, noE9, 11))
  grafo.adicionaAresta(Aresta(noE2, noE10, 4))

  grafo.adicionaAresta(Aresta(noE3, noE9, 10))
  grafo.adicionaAresta(Aresta(noE3, noE13, 11))
  grafo.adicionaAresta(Aresta(noE3, noE4, 7))
  #grafo.adicionaAresta(Aresta(noE3, noE2, 9))
  
  grafo.adicionaAresta(Aresta(noE4, noE8, 13))
  grafo.adicionaAresta(Aresta(noE4, noE13, 11))
  grafo.adicionaAresta(Aresta(noE4, noE5, 13))
  #grafo.adicionaAresta(Aresta(noE4, noE3, 7))

  grafo.adicionaAresta(Aresta(noE5, noE6, 3))
  grafo.adicionaAresta(Aresta(noE5, noE7, 2))
  #grafo.adicionaAresta(Aresta(noE5, noE4, 13))
  grafo.adicionaAresta(Aresta(noE5, noE8, 21))
  
  # grafo.adicionaAresta(Aresta(noE6, noE5, 3))

  # grafo.adicionaAresta(Aresta(noE7, noE5, 2))

  grafo.adicionaAresta(Aresta(noE8, noE12, 7))
  # grafo.adicionaAresta(Aresta(noE8, noE9, 9))
  # grafo.adicionaAresta(Aresta(noE8, noE4, 13))
  # grafo.adicionaAresta(Aresta(noE8, noE5, 21))

  grafo.adicionaAresta(Aresta(noE9, noE8, 9))
  grafo.adicionaAresta(Aresta(noE9, noE11, 12))
  #grafo.adicionaAresta(Aresta(noE9, noE2, 11))
  # grafo.adicionaAresta(Aresta(noE9, noE3, 10))

  # grafo.adicionaAresta(Aresta(noE10, noE2, 4))

  #grafo.adicionaAresta(Aresta(noE11, noE9, 12))

  # grafo.adicionaAresta(Aresta(noE12, noE8, 7))

  #grafo.adicionaAresta(Aresta(noE13, noE4, 11))
  grafo.adicionaAresta(Aresta(noE13, noE14, 5))
  #grafo.adicionaAresta(Aresta(noE13, noE3, 13))

  #grafo.adicionaAresta(Aresta(noE14, noE13, 5))


  custo, caminho = grafo.aEstrela(noE1, noE12)
  print('Caminho: {}\nCusto Total: {}'.format(' -> '.join(caminho), custo))


'''
Fila de prioridade - Heap minimo a partir do f(n)
Objetivo: Sempre retirar o menor f(n)

Algoritmo executando:

1 Passo
  Fila: S
    retira S e calcula seus sucessores
    Fila: []
    Para cada sucessor, calcula F(n)
      Calcula A
      Adiciona A na Fila de prioridade
      Fila: A
      Calcula B
      Adiciona B na Fila de prioridade
      Fila: B, A

2 Passo
  Fila: B, A
    retira B e calcula seus sucessores (possui menor f(n))
    Fila: A
    Para cada sucessor, calcula F(n)
      Calcula G
      Adiciona G na Fila de prioridade
      Fila: A, G
      
3 Passo
  Fila: A, G
    retira A e calcula seus sucessores (possui menor f(n))
    Fila: G
    Para cada sucessor, calcula F(n)
      Calcula G, vindo de A
      Adiciona G na Fila de prioridade
      Fila: G, G

4 Passo
  Fila: G, G
    retira G e calcula seus sucessores (possui menor f(n))
    Fila: G
    Para cada sucessor, calcula F(n)      
      Nao tem
    Fila: G

5 Passo
  Fila: G
    retira G e calcula seus sucessores (possui menor f(n))
    Fila: G
    Para cada sucessor, calcula F(n)      
      Nao tem
    Fila: []

Algoritmo finaliza quando a fila esta vazia
'''