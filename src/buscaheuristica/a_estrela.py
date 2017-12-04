class AEstrela(object):

  def __init__(self, vertices):
    # lista de vertices ja calculados
    self.vertices_abertos = []
    # lista de vertices ainda nao calculados
    self.vertices_fechados = []
    self.vertices = vertices

  def reconstroi_caminho(self, v_antecessor, v_atual):
    caminho = [v_atual.chave]
    custo = v_atual.f_de_n
    chave_v_atual = v_atual.chave
    while v_antecessor[chave_v_atual]:
      chave_v_atual = v_antecessor[chave_v_atual].chave
      caminho.append(chave_v_atual)
    caminho.reverse() 
    return (caminho, custo)

  def get_v_adjacentes(self, vertice):
    v_adjacentes = []
    for aresta in vertice.arestas_adj:
      v_adjacentes.append(aresta.v_destino)
    return v_adjacentes

  def distancia_entre(self, v_atual, v_adj):
    for aresta_adj_atual in v_atual.arestas_adj:
      if aresta_adj_atual.v_destino == v_adj:
        return aresta_adj_atual.distancia

  def recupera_menor_f(self):
    menor = self.vertices_abertos[0]
    for v in self.vertices_abertos:
      if v.f_de_n < menor.f_de_n:
        menor = v
    return menor

  def a_estrela(self, v_inicio, v_final):
    # Inicia pelo primeiro vertice
    self.vertices_abertos.append(v_inicio)

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    
    # Para cada vertice, eh salvo o seu antecessor que possui o melhor caminho,
    # caso ele tenha muitos caminhos
    v_antecessor = {}
    
    # For each node, the cost of getting from the start node to that node.
    # Para cada vertice, a distancia do inicio ate o vertice atual
    distancia_ate_n = {}

    # Preenche
    for v in vertices:
      v_antecessor[v.chave] = None
      distancia_ate_n[v.chave] = None

    # A distancia do inicio para o inicio eh zero
    distancia_ate_n[v_inicio.chave] = 0

    # Para o primeiro vertice, f(n) = g(n) + h(n) = 0 + h(n)
    v_inicio.f_de_n = v_inicio.h_de_n

    # Enquanto existir nos em aberto
    while len(self.vertices_abertos) != 0:
        v_atual = self.recupera_menor_f()
        if v_atual == v_final:
            return self.reconstroi_caminho(v_antecessor, v_atual) # Condicao de parada com sucesso!

        self.vertices_abertos.remove(v_atual) # Remove atual dos vertices abertos
        self.vertices_fechados.append(v_atual) # Adiciona atual aos vertices fechados

        for v_adj in self.get_v_adjacentes(v_atual):
            if v_adj in self.vertices_fechados:
                continue		# Ignore the neighbor which is already evaluated.

            if v_adj not in self.vertices_abertos: # Um vertice novo
                self.vertices_abertos.append(v_adj)
            
            # Distancia do vertice atual ate o seu vertice adjacente
            # Adiciona baldeacao, trafico
            novo_g_de_n = distancia_ate_n[v_atual.chave] + self.distancia_entre(v_atual, v_adj)
            if distancia_ate_n[v_adj.chave]:
              if novo_g_de_n >= distancia_ate_n[v_adj.chave]:
                continue		# Este nao eh o melhor caminho         

            # melhor caminho ate agora
            v_antecessor[v_adj.chave] = v_atual
            distancia_ate_n[v_adj.chave] = novo_g_de_n
            # f(n) = g(n) + h(n)
            v_adj.f_de_n = distancia_ate_n[v_adj.chave] + v_adj.h_de_n

    return None

if __name__ == '__main__':
  from vertice import Vertice
  from aresta import Aresta

  # noS = Vertice('S', 3)
  # noA = Vertice('A', 2)
  # noB = Vertice('B', 1)
  # noG = Vertice('G', 0)

  # vertices = [noS, noA, noB, noG]

  # noS.add_aresta_adj(Aresta(noA, 2))
  # noS.add_aresta_adj(Aresta(noB, 2))
  # noA.add_aresta_adj(Aresta(noG, 2))
  # noB.add_aresta_adj(Aresta(noG, 3))
  # noB.add_aresta_adj(Aresta(noS, 2))

  # caminho = AEstrela(vertices).a_estrela(noS, noG)
  # print('Caminho {}'.format(' -> '.join(caminho)))

  vertices = []
  noE1 = Vertice('E1', 30)
  vertices.append(noE1)
  noE2 = Vertice('E2', 23)
  vertices.append(noE2)
  noE3 = Vertice('E3', 21)
  vertices.append(noE3)
  noE4 = Vertice('E4', 21)
  vertices.append(noE4)
  noE5 = Vertice('E5', 27)
  vertices.append(noE5)
  noE6 = Vertice('E6', 30)
  vertices.append(noE6)
  noE7 = Vertice('E7', 28)
  vertices.append(noE7)
  noE8 = Vertice('E8', 7)
  vertices.append(noE8)
  noE9 = Vertice('E9', 12)
  vertices.append(noE9)
  noE10 = Vertice('E10', 27)
  vertices.append(noE10)
  noE11 = Vertice('E11', 15)
  vertices.append(noE11)
  noE12 = Vertice('E12', 0)
  vertices.append(noE12)
  noE13 = Vertice('E13', 31)
  vertices.append(noE13)
  noE14 = Vertice('E14', 37)
  vertices.append(noE14)

  noE1.add_aresta_adj(Aresta(noE2, 11))
  noE2.add_aresta_adj(Aresta(noE1, 11))
  
  noE2.add_aresta_adj(Aresta(noE3, 9))
  noE2.add_aresta_adj(Aresta(noE9, 11))
  noE2.add_aresta_adj(Aresta(noE10, 4))

  noE3.add_aresta_adj(Aresta(noE9, 10))
  noE3.add_aresta_adj(Aresta(noE13, 11))
  noE3.add_aresta_adj(Aresta(noE4, 7))
  
  noE4.add_aresta_adj(Aresta(noE8, 13))
  noE4.add_aresta_adj(Aresta(noE13, 11))
  noE4.add_aresta_adj(Aresta(noE5, 13))

  noE5.add_aresta_adj(Aresta(noE6, 3))
  noE5.add_aresta_adj(Aresta(noE7, 2))
  noE5.add_aresta_adj(Aresta(noE8, 21))

  noE8.add_aresta_adj(Aresta(noE12, 7))
  
  noE9.add_aresta_adj(Aresta(noE8, 9))
  noE9.add_aresta_adj(Aresta(noE11, 12))

  noE13.add_aresta_adj(Aresta(noE14, 5))

  caminho, custo = AEstrela(vertices).a_estrela(noE1, noE12)
  print('Menor Caminho: {}\nCusto: {}'.format(' -> '.join(caminho), custo))

  '''
  Para cada vertice:
    Label
    Distancia do vertice N ate o vertice Final
  
  Para aresta
    Cor - Para verificar baldeacao
    Distancia entre os vertices
    Quais sao os vertices
    Custo adicional previsto pelo Aprendizado de Maquina, referente ao trafego
  '''
